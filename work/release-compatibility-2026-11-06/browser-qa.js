async (page) => {
  const errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  await page.reload();
  await page.waitForFunction(()=>window.releaseReview?.getSnapshot().loaded);
  const catalog=await page.evaluate(()=>window.releaseReview.getCatalog());
  const findings=[];
  const check=(ok,name)=>{if(!ok)throw new Error(name);findings.push(name)};
  check(catalog.length===47,'47 editions available');
  check(catalog.filter(p=>p.changed).length===45,'45 repaired / 2 preserved');
  for(const pet of catalog){
    await page.getByLabel('选择角色 / 版本').selectOption(pet.id);
    await page.waitForFunction(id=>{const s=window.releaseReview.getSnapshot();return s.id===id&&s.loaded},pet.id);
    if(pet.changed)await page.getByRole('button',{name:'定位原版闭眼',exact:true}).click();
    const visual=await page.evaluate(()=>{
      const a=document.querySelector('#before').getContext('2d').getImageData(0,0,384,416).data;
      const b=document.querySelector('#after').getContext('2d').getImageData(0,0,384,416).data;
      let occupied=0,differences=0;for(let i=0;i<a.length;i+=4){if(a[i+3])occupied++;for(let c=0;c<4;c++)if(a[i+c]!==b[i+c]){differences++;break}}
      return {occupied,differences,snapshot:window.releaseReview.getSnapshot()};
    });
    check(visual.occupied>1000 && (pet.changed?visual.differences>0:visual.differences===0),pet.id+' actual before/after pixels');
    check((await page.getByRole('button',{name:'定位原版闭眼',exact:true}).isEnabled())===pet.changed,pet.id+' applicable inspection control');
  }
  const sample=await page.evaluate(()=>[0,1679,1680,6599,6600].map(window.releaseReview.frameAt));
  check(JSON.stringify(sample)==='[0,0,1,5,0]','native 6.6-second timing boundaries');
  await page.setViewportSize({width:1440,height:1000});
  await page.getByLabel('选择角色 / 版本').selectOption('furina');
  await page.waitForFunction(()=>window.releaseReview.getSnapshot().id==='furina'&&window.releaseReview.getSnapshot().loaded);
  await page.getByRole('button',{name:'定位原版闭眼',exact:true}).click();
  await page.screenshot({path:'output/playwright/pet-all-releases-desktop.png',fullPage:true});
  await page.setViewportSize({width:390,height:844});
  await page.screenshot({path:'output/playwright/pet-all-releases-mobile.png',fullPage:true});
  const mobile=await page.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,buttons:[...document.querySelectorAll('button')].map(e=>e.getBoundingClientRect().height),selectWidth:document.querySelector('select').getBoundingClientRect().width}));
  check(mobile.scrollWidth<=mobile.width,'390px viewport has no horizontal overflow');
  check(mobile.buttons.every(h=>h>=44),'touch controls at least 44px');
  await page.getByLabel('播放进度').press('Home');
  await page.getByLabel('播放进度').press('PageUp');
  check((await page.evaluate(()=>window.releaseReview.getSnapshot())).elapsed>0,'keyboard timeline works');
  await page.getByRole('button',{name:'播放',exact:true}).click();
  await page.waitForFunction(()=>window.releaseReview.getSnapshot().playing);
  await page.getByRole('button',{name:'暂停',exact:true}).click();
  check(!(await page.evaluate(()=>window.releaseReview.getSnapshot())).playing,'play and pause work');
  await page.emulateMedia({reducedMotion:'reduce'});
  await page.reload();await page.waitForFunction(()=>window.releaseReview?.getSnapshot().loaded);
  check(!(await page.evaluate(()=>window.releaseReview.getSnapshot())).playing,'reduced motion starts paused');
  await page.getByRole('button',{name:'播放',exact:true}).click();
  await page.waitForFunction(()=>window.releaseReview.getSnapshot().elapsed>50);
  check((await page.evaluate(()=>window.releaseReview.getSnapshot())).playing,'explicit playback remains available');
  await page.goto('file:///home/ubuntu23/Bureau/codex-anime-pets/output/pet-release-comparison.html');
  await page.waitForFunction(()=>window.releaseReview?.getSnapshot().loaded);
  check((await page.evaluate(()=>window.releaseReview.getSnapshot())).count===47,'offline standalone HTML loads all 47');
  check(errors.length===0,'no JavaScript runtime errors');
  await page.setViewportSize({width:1440,height:1000});
  return {ok:true,checks:findings.length,findings,mobile,errors};
}
