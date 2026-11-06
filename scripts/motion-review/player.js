(() => {
  'use strict';
  const data = window.PET_REVIEW_DATA;
  const $ = id => document.getElementById(id);
  const names = { idle: '待机', running: '处理中', waiting: '等待输入', review: '审阅', failed: '失败' };
  const rows = { idle: 0, running: 7, waiting: 6, review: 8, failed: 5 };
  const durations = {
    idle: [280,110,110,140,140,320], running: [120,120,120,120,120,220],
    waiting: [150,150,150,150,150,260], review: [150,150,150,150,150,280],
    failed: [140,140,140,140,140,140,140,240]
  };
  const sum = xs => xs.reduce((a,b) => a+b, 0);
  const slowIdle = durations.idle.map(ms => ms * 6);
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const settings = {
    timing: { title: '把预览，放回真实的时间里。', description: '同一份原版素材：左侧按旧 GIF 循环，右侧还原本机客户端的播放策略。', type: '仅改预览时序', before: '原版 GIF 时序', after: '客户端时序', finding: '原版展示较快，实机更安静。', copy: '待机一轮从展示用的 1.1 秒还原为 6.6 秒。选择处理中，可看到客户端在约 2.46 秒后回到待机；此项不改宠物素材。', value: '1.1 → 6.6', unit: '秒 / 待机一轮' },
    idle: { title: '慢下来，依然看得见呼吸。', description: '两侧都按 6.6 秒一轮播放；候选行保留睁眼，以肩部和发梢的细小变化表达呼吸。', type: '整行重制 · idle', before: '原版待机', after: '候选待机', finding: '去掉慢速下的长时间闭眼。', copy: '原版闭眼帧在慢速下会停留约 0.66–0.84 秒。候选六帧保持睁眼，采用收敛的呼吸变化；脚部锚定，首尾回到接近的姿态。', value: '6 / 6', unit: '帧保持睁眼 · 同速对比' },
    states: { title: '工作姿态，保留为可选比较。', description: '此项属于视觉偏好，尚未证明适合批量替换。页面保留新旧姿态对照，下载包中的工作动作保持原版。', type: '可选 · 未纳入下载', before: '原版动作', after: '可选候选', finding: '先保留选择，不批量替换。', copy: '下载包只修复待机长时间闭眼。这里的工作姿态用于比较；等待输入、审阅、失败沿用原版，客户端仍按三轮后回到待机的现有策略播放。', value: '0.82', unit: '秒 / 第一轮工作动作' }
  };
  let petIndex = 0, mode = 'timing', state = 'idle', elapsed = 0;
  let playing = !reduced.matches, lastTick = null, loaded = false, loadToken = 0;
  let images = null, large = false;
  const maxTime = () => mode === 'idle' ? 6600 : 12000;

  function frameAt(ms, timing) {
    let t = ((ms % sum(timing)) + sum(timing)) % sum(timing);
    for (let i=0;i<timing.length;i++) { if (t < timing[i]) return i; t -= timing[i]; }
    return timing.length-1;
  }
  function sample(ms, action, native) {
    if (!native) return { state: action, frame: frameAt(ms, durations[action]), phase: 'loop' };
    if (action === 'idle') return { state: 'idle', frame: frameAt(ms, slowIdle), phase: 'idle' };
    const end = sum(durations[action]) * 3;
    return ms < end
      ? { state: action, frame: frameAt(ms, durations[action]), phase: 'action' }
      : { state: 'idle', frame: frameAt(ms-end, slowIdle), phase: 'idle-tail' };
  }
  function sprite(canvas, image, action, frame) {
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0,0,canvas.width,canvas.height);
    ctx.imageSmoothingEnabled = true; ctx.imageSmoothingQuality = 'high';
    ctx.drawImage(image,frame*192,rows[action]*208,192,208,0,0,canvas.width,canvas.height);
  }
  function strip(canvas, image, action) {
    const n = durations[action].length;
    canvas.width=n*192;
    const ctx = canvas.getContext('2d'); ctx.clearRect(0,0,canvas.width,canvas.height);
    for(let i=0;i<n;i++) {
      ctx.fillStyle = i%2 ? '#eff0e8' : '#fafaf5'; ctx.fillRect(i*192,0,192,208);
      if(i<n) ctx.drawImage(image,i*192,rows[action]*208,192,208,i*192,0,192,208);
      ctx.strokeStyle = '#d9dfd3'; ctx.strokeRect(i*192+.5,.5,191,207);
    }
  }
  function loadImage(src) {
    return new Promise((resolve,reject) => { const im=new Image(); im.onload=()=>resolve(im); im.onerror=()=>reject(Error('图集加载失败')); im.src=src; });
  }
  async function selectPet(i) {
    petIndex=i; loaded=false; const token=++loadToken; elapsed=0;
    document.querySelectorAll('.character').forEach((button,j)=>button.setAttribute('aria-pressed',String(i===j)));
    $('load-status').className='load-status'; $('load-status').textContent='正在加载角色素材…';
    const pet=data.pets[i];
    $('download').disabled=!pet.package;
    $('download').setAttribute('aria-disabled',String(!pet.package));
    $('download-note').textContent=pet.package ? '仅改待机 · 独立候选 ID' : '候选素材准备中';
    try {
      const pair=await Promise.all([loadImage(pet.beforeAtlas),loadImage(pet.afterAtlas)]);
      if(token!==loadToken)return;
      images=pair;loaded=true;lastTick=null;$('load-status').textContent=pet.ready?'':'候选素材生成中；当前两侧暂显示原版。';
      updateStrips(); drawStateTiles(); render();
    } catch(error) { if(token===loadToken){$('load-status').textContent='素材加载失败，请重新打开 HTML 或切换角色重试。';$('load-status').classList.add('is-error');} }
  }
  function render() {
    if(!loaded)return;
    const action = mode==='idle'?'idle':state;
    const a=sample(elapsed,action,mode!=='timing'); const b=sample(elapsed,action,true);
    sprite($('before-canvas'),images[0],a.state,a.frame);
    sprite($('after-canvas'),images[mode==='timing'?0:1],b.state,b.frame);
    $('before-state').textContent=names[a.state]; $('after-state').textContent=names[b.state]+(b.phase==='idle-tail'?' · 三轮后回落':'');
    $('before-frame').textContent=`FRAME ${String(a.frame+1).padStart(2,'0')} / ${durations[a.state].length}`;
    $('after-frame').textContent=`FRAME ${String(b.frame+1).padStart(2,'0')} / ${durations[b.state].length}`;
    $('seek').value=(elapsed/1000).toFixed(2);
    $('time').textContent=`${(elapsed/1000).toFixed(2).padStart(5,'0')} / ${(maxTime()/1000).toFixed(2)}s`;
    $('before-canvas').setAttribute('aria-label',`${data.pets[petIndex].name}，原版，${names[a.state]}，第${a.frame+1}帧`);
    $('after-canvas').setAttribute('aria-label',`${data.pets[petIndex].name}，${mode==='timing'?'客户端时序':'候选'}，${names[b.state]}，第${b.frame+1}帧`);
  }
  function updateStrips() {
    if(!loaded)return;const action=mode==='idle'?'idle':state;
    strip($('before-strip'),images[0],action);strip($('after-strip'),images[mode==='timing'?0:1],action);
    $('strip-caption').textContent=`查看本行动作的 ${durations[action].length} 个原生帧`;
    $('after-strip-label').textContent=mode==='timing'?'B · 客户端时序（同份原版素材）':'B · 候选';
    $('before-meta').textContent=mode==='timing'?'GIF / LOOP':'NATIVE / SAME CLOCK';
    $('after-meta').textContent=mode==='timing'?'NATIVE / 26.1007':'NATIVE / SAME CLOCK';
    document.querySelectorAll('[data-state]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.state===action)));
  }
  function drawStateTiles() {
    if(!loaded)return;
    document.querySelectorAll('.state-tile').forEach(button=>{
      const canvases=button.querySelectorAll('canvas');
      sprite(canvases[0],images[0],button.dataset.state,0);sprite(canvases[1],images[1],button.dataset.state,0);
    });
  }
  function selectState(action) {
    state=action;elapsed=0;lastTick=null;updateStrips();render();
  }
  function setPlaying(value) {
    playing=value;lastTick=null;$('play').innerHTML=value?'暂停 <span aria-hidden="true">Ⅱ</span>':'播放 <span aria-hidden="true">▷</span>';
    $('play').setAttribute('aria-label',value?'暂停播放':'播放动画');
  }
  function selectMode(value) {
    mode=value; elapsed=0;lastTick=null;
    if(mode==='idle')state='idle';else if(mode==='states')state='running';
    const s=settings[mode];
    for(const [id,text] of Object.entries({'study-title':s.title,'study-description':s.description,'change-type':s.type,'before-label':s.before,'after-label':s.after,'finding-title':s.finding,'finding-copy':s.copy,'measurement-value':s.value,'measurement-unit':s.unit}))$(id).textContent=text;
    $('finding-number').textContent=`${['timing','idle','states'].indexOf(mode)+1}`.padStart(2,'0')+' / OBSERVATION';
    $('study-panel').setAttribute('aria-labelledby','tab-'+mode);
    document.querySelectorAll('[data-mode]').forEach(button=>{const selected=button.dataset.mode===mode;button.setAttribute('aria-selected',String(selected));button.tabIndex=selected?0:-1;});
    $('states').hidden=mode==='states';$('state-gallery').hidden=mode!=='states';
    $('states').querySelectorAll('button').forEach(button=>{button.hidden=mode==='idle'&&button.dataset.state!=='idle';button.disabled=mode==='idle'&&button.dataset.state!=='idle';});
    $('seek').max=maxTime()/1000;
    $('playback-note').textContent=reduced.matches?'已遵循系统减少动态效果：默认暂停，可手动拖动时间轴或点击播放。':mode==='timing'?'两侧共用时间轴。切换“处理中”，观察 2.46 秒后的播放差异。':mode==='idle'?'两侧均为 6.6 秒一轮。可暂停并拖动时间轴，检查眼睛、肩部与发梢。':'两侧均按实机策略播放三轮后回到待机。下方可检查四种状态的首帧。';
    updateStrips();render();
  }
  data.pets.forEach((pet,i)=>{
    const button=document.createElement('button');button.className='character';button.type='button';button.setAttribute('aria-pressed',String(i===0));
    const canvas=document.createElement('canvas');canvas.width=96;canvas.height=116;canvas.setAttribute('aria-hidden','true');
    const text=document.createElement('span');const title=document.createElement('strong');title.textContent=pet.name;const english=document.createElement('small');english.textContent=pet.english;text.append(title,english);button.append(canvas,text);button.addEventListener('click',()=>selectPet(i));$('characters').append(button);
    loadImage(pet.beforeAtlas).then(im=>{const c=canvas.getContext('2d');c.drawImage(im,0,0,192,208,0,4,96,104);}).catch(()=>{});
  });
  Object.entries(names).forEach(([action,name])=>{
    const button=document.createElement('button');button.type='button';button.dataset.state=action;button.textContent=name;button.setAttribute('aria-pressed',String(action==='idle'));button.addEventListener('click',()=>selectState(action));$('states').append(button);
  });
  ['running','waiting','review','failed'].forEach(action=>{
    const button=document.createElement('button');button.className='state-tile';button.type='button';button.dataset.state=action;button.setAttribute('aria-pressed',String(action==='running'));button.setAttribute('aria-label','检查'+names[action]+'状态');
    const label=document.createElement('span');label.textContent=names[action];const pair=document.createElement('div');pair.className='mini-pair';const a=document.createElement('canvas'),b=document.createElement('canvas');a.width=b.width=192;a.height=b.height=208;a.setAttribute('aria-hidden','true');b.setAttribute('aria-hidden','true');const arrow=document.createElement('b');arrow.textContent='→';pair.append(a,arrow,b);const note=document.createElement('small');note.textContent=action==='running'?'可选 · 未纳入下载':'沿用原版';button.append(label,pair,note);button.addEventListener('click',()=>selectState(action));$('state-gallery').append(button);
  });
  document.querySelectorAll('[data-mode]').forEach(button=>button.addEventListener('click',()=>selectMode(button.dataset.mode)));
  $('play').addEventListener('click',()=>setPlaying(!playing));
  $('restart').addEventListener('click',()=>{elapsed=0;lastTick=null;render();});
  $('seek').addEventListener('input',event=>{elapsed=Number(event.target.value)*1000;lastTick=null;render();});
  $('background').addEventListener('click',()=>{const active=document.body.classList.toggle('dark-stages');$('background').setAttribute('aria-pressed',String(active));$('background').textContent=active?'浅色背景':'深色背景';});
  $('download').addEventListener('click',async()=>{
    const pet=data.pets[petIndex];if(!pet.package)return;
    const button=$('download');button.disabled=true;button.textContent='正在准备下载…';
    try{
      const blob=await (await fetch(pet.package)).blob();const url=URL.createObjectURL(blob);
      const link=document.createElement('a');link.href=url;link.download=pet.packageFilename;document.body.append(link);link.click();link.remove();setTimeout(()=>URL.revokeObjectURL(url),30000);
    }catch(error){$('load-status').textContent='下载未完成，请再次点击下载按钮重试。';$('load-status').classList.add('is-error');}
    finally{button.disabled=!data.pets[petIndex].package;button.innerHTML='下载待机优化包 <span aria-hidden="true">↓</span>';}
  });
  $('size').addEventListener('click',()=>{large=!large;document.body.classList.toggle('large-sprites',large);$('size').setAttribute('aria-pressed',String(large));$('size').textContent=large?'还原尺寸':'放大检查';updateSizeLabels();});
  function updateSizeLabels(){document.querySelectorAll('.stage-scale').forEach(label=>label.textContent=large?'192 × 208 · 放大检查':innerWidth<=700?'192 × 208 · 适屏显示':'192 × 208 · 原生显示');}
  window.addEventListener('resize',updateSizeLabels);
  document.querySelector('.study-tabs').addEventListener('keydown',event=>{
    if(!['ArrowLeft','ArrowRight','Home','End'].includes(event.key))return;
    event.preventDefault();const modes=['timing','idle','states'];let i=modes.indexOf(mode);i=event.key==='Home'?0:event.key==='End'?2:(i+(event.key==='ArrowRight'?1:2))%3;selectMode(modes[i]);$('tab-'+modes[i]).focus();
  });
  document.addEventListener('visibilitychange',()=>{lastTick=null;});
  reduced.addEventListener('change',event=>{if(event.matches)setPlaying(false);selectMode(mode);});
  function tick(now){if(playing&&loaded&&!document.hidden){if(lastTick!==null)elapsed=(elapsed+Math.min(now-lastTick,100))%maxTime();lastTick=now;render();}else lastTick=null;requestAnimationFrame(tick);}
  $('verification-status').textContent=data.pets.every(p=>p.ready)?'3 位角色 · 候选校验通过':'候选生成中';
  $('qa-summary').textContent=data.qaSummary;
  // Read-only diagnostics make the displayed timing and asset provenance inspectable.
  window.petReview={sample,frameAt,getSnapshot:()=>({pet:data.pets[petIndex].id,mode,state,elapsed,playing,loaded,before:sample(elapsed,mode==='idle'?'idle':state,mode!=='timing'),after:sample(elapsed,mode==='idle'?'idle':state,true)}),getAssetInfo:()=>data.pets.map(({id,ready,qa})=>({id,ready,qa}))};
  selectMode('timing');setPlaying(playing);updateSizeLabels();selectPet(0);requestAnimationFrame(tick);
})();
