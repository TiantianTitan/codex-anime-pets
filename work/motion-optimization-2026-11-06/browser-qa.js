async (page) => {
  const findings=[];
  const check=(condition,label)=>{if(!condition)throw new Error(label);findings.push(label);};
  await page.waitForFunction(()=>window.petReview?.getSnapshot().loaded);
  if(await page.evaluate(()=>window.petReview.getSnapshot().playing))await page.getByRole('button',{name:'暂停播放',exact:true}).click();
  await page.setViewportSize({width:1365,height:1000});
  const ids=['xiao','dan-heng-imbibitor-lunae','jing-yuan'];
  for(let i=0;i<ids.length;i++){
    await page.locator('.character').nth(i).click();
    await page.waitForFunction(id=>window.petReview.getSnapshot().loaded&&window.petReview.getSnapshot().pet===id,ids[i]);
    for(const mode of ['timing','idle','states']){
      await page.locator('#tab-'+mode).click();
      const result=await page.evaluate(()=>{
        const a=document.querySelector('#before-canvas').getContext('2d').getImageData(0,0,384,416).data;
        const b=document.querySelector('#after-canvas').getContext('2d').getImageData(0,0,384,416).data;
        let nonempty=0,different=0;for(let p=0;p<a.length;p+=4){if(a[p+3])nonempty++;if(a[p]!==b[p]||a[p+1]!==b[p+1]||a[p+2]!==b[p+2]||a[p+3]!==b[p+3])different++;}
        return {...window.petReview.getSnapshot(),nonempty,different};
      });
      check(result.mode===mode&&result.loaded&&result.nonempty>1000,`${ids[i]} ${mode}: sprites loaded and controls select mode`);
      check(mode==='timing'?result.different===0:result.different>100,`${ids[i]} ${mode}: timing uses identical assets; artwork comparison uses actual new pixels`);
    }
  }
  const timing=await page.evaluate(()=>{
    const p=window.petReview;return {pre:p.sample(2459,'running',true),post:p.sample(2460,'running',true),raw:p.sample(3600,'running',false),idleEnd:p.sample(6599,'idle',true),idleStart:p.sample(6600,'idle',true)};
  });
  check(timing.pre.state==='running'&&timing.post.state==='idle','native working boundary is exactly 2460 ms');
  check(timing.raw.state==='running','old GIF loop remains working beyond native boundary');
  check(timing.idleEnd.frame===5&&timing.idleStart.frame===0,'native idle loop is exactly 6600 ms');
  await page.locator('.character').nth(0).click();await page.waitForFunction(()=>window.petReview.getSnapshot().loaded&&window.petReview.getSnapshot().pet==='xiao');
  await page.locator('#tab-timing').click();await page.locator('#states [data-state="running"]').click();
  await page.locator('#seek').press('Home');await page.locator('#seek').press('PageUp');await page.locator('#seek').press('PageUp');await page.locator('#seek').press('PageUp');
  const range=await page.evaluate(()=>window.petReview.getSnapshot());check(range.before.state==='running'&&range.after.state==='idle','keyboard timeline exposes three-cycle fallback difference');
  await page.screenshot({path:'output/playwright/pet-motion-timing-desktop.png',fullPage:true});
  await page.locator('#tab-idle').click();await page.locator('#seek').press('Home');for(let i=0;i<3;i++)await page.locator('#seek').press('PageUp');
  check(await page.locator('#states button:visible').count()===1,'idle comparison hides unrelated state controls');
  await page.screenshot({path:'output/playwright/pet-motion-idle-desktop.png',fullPage:true});
  await page.locator('#tab-states').click();
  check((await page.locator('#change-type').textContent()).includes('未纳入下载'),'working-pose exploration is explicitly excluded from the download');
  await page.screenshot({path:'output/playwright/pet-motion-states-desktop.png',fullPage:true});
  await page.getByRole('button',{name:'检查失败状态',exact:true}).click();
  check(await page.locator('#before-strip').getAttribute('width')==='1536','eight-frame failure strip displays all frames');
  await page.getByRole('button',{name:'检查处理中状态',exact:true}).click();
  const downloadPromise=page.waitForEvent('download');await page.getByRole('button',{name:'下载待机优化包',exact:false}).click();const download=await downloadPromise;
  await download.saveAs('output/playwright/downloaded-xiao-idle-candidate.zip');check(download.suggestedFilename()==='xiao-idle-candidate.zip','embedded idle-only package downloads with the correct name');
  await page.locator('#tab-idle').click();await page.locator('#tab-idle').press('ArrowRight');check(await page.locator('#tab-states').getAttribute('aria-selected')==='true','keyboard tabs switch mode and focus');
  await page.getByRole('button',{name:'深色背景',exact:true}).click();check(await page.locator('#background').getAttribute('aria-pressed')==='true','dark inspection background toggles');await page.getByRole('button',{name:'浅色背景',exact:true}).click();
  await page.getByRole('button',{name:'放大检查',exact:true}).click();check(await page.locator('#size').getAttribute('aria-pressed')==='true','inspection size toggles');await page.getByRole('button',{name:'还原尺寸',exact:true}).click();
  await page.setViewportSize({width:390,height:844});await page.locator('#tab-idle').click();await page.locator('#seek').press('Home');for(let i=0;i<3;i++)await page.locator('#seek').press('PageUp');
  await page.screenshot({path:'output/playwright/pet-motion-idle-mobile.png',fullPage:true});
  const layout=await page.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,overflow:[...document.querySelectorAll('button,h1,h2,h3,p,summary')].filter(el=>{const b=el.getBoundingClientRect();return b.width>0&&(b.right>innerWidth+1||b.left< -1);}).map(el=>el.id||el.textContent.slice(0,30)),targets:[...document.querySelectorAll('button')].filter(el=>{const b=el.getBoundingClientRect();return b.width>0&&b.height>0&&b.height<43;}).map(el=>({text:el.textContent,height:el.getBoundingClientRect().height}))}));
  check(layout.scrollWidth<=layout.width&&layout.overflow.length===0,'390px mobile layout has no horizontal overflow');check(layout.targets.length===0,'mobile buttons meet 44px touch height');
  await page.emulateMedia({reducedMotion:'reduce'});await page.reload();await page.waitForFunction(()=>window.petReview?.getSnapshot().loaded);
  check(await page.evaluate(()=>!window.petReview.getSnapshot().playing),'reduced motion starts paused');
  await page.getByRole('button',{name:'播放动画',exact:true}).click();check(await page.evaluate(()=>window.petReview.getSnapshot().playing),'explicit play remains available with reduced motion');await page.getByRole('button',{name:'暂停播放',exact:true}).click();
  await page.emulateMedia({reducedMotion:'no-preference'});await page.setViewportSize({width:1365,height:1000});
  await page.goto('file:///home/ubuntu23/Bureau/codex-anime-pets/output/pet-motion-comparison.html');await page.waitForFunction(()=>window.petReview?.getSnapshot().loaded);
  check(await page.evaluate(()=>window.PET_REVIEW_DATA.pets.every(p=>p.ready)),'standalone file loads all three approved candidates without a server');
  check(await page.evaluate(()=>window.PET_REVIEW_DATA.pets.every(p=>p.packageQa.scope==='idle-only'&&p.packageQa.preservedUsedCellCount===68)),'all download packages contain only the demonstrated idle fix');
  if(await page.evaluate(()=>window.petReview.getSnapshot().playing))await page.getByRole('button',{name:'暂停播放',exact:true}).click();
  await page.locator('#tab-idle').click();await page.locator('#seek').press('Home');for(let i=0;i<3;i++)await page.locator('#seek').press('PageUp');
  return {ok:true,checks:findings.length,findings,mobile:layout,timing};
}
