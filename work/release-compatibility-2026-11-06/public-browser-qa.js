async (page) => {
  const errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.waitForFunction(()=>window.releaseReview?.getSnapshot().loaded);
  const catalog=await page.evaluate(()=>window.releaseReview.getCatalog());
  for(const p of catalog){
    await page.getByLabel('选择角色 / 版本').selectOption(p.id);
    await page.waitForFunction(id=>{const s=window.releaseReview.getSnapshot();return s.id===id&&s.loaded},p.id);
    if(p.changed)await page.getByRole('button',{name:'定位原版闭眼',exact:true}).click();
  }
  if(catalog.length!==47||errors.length)throw new Error(JSON.stringify({count:catalog.length,errors}));
  await page.setViewportSize({width:1440,height:1000});
  await page.getByLabel('选择角色 / 版本').selectOption('furina');
  await page.waitForFunction(()=>window.releaseReview.getSnapshot().id==='furina'&&window.releaseReview.getSnapshot().loaded);
  await page.getByRole('button',{name:'定位原版闭眼',exact:true}).click();
  await page.screenshot({path:'docs/pet-idle-comparison.png',fullPage:true});
  return {ok:true,localHttpEditionLoads:catalog.length,errors};
}
