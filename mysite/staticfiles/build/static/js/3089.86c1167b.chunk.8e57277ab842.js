"use strict";(self.webpackChunkparticles=self.webpackChunkparticles||[]).push([[3089],{3089:(e,t,i)=>{i.d(t,{LifeUpdater:()=>c});var n=i(4409);class s extends n.PV{constructor(){super(),this.sync=!1}load(e){e&&(super.load(e),void 0!==e.sync&&(this.sync=e.sync))}}class a extends n.PV{constructor(){super(),this.sync=!1}load(e){e&&(super.load(e),void 0!==e.sync&&(this.sync=e.sync))}}class o{constructor(){this.count=0,this.delay=new s,this.duration=new a}load(e){e&&(void 0!==e.count&&(this.count=e.count),this.delay.load(e.delay),this.duration.load(e.duration))}}class c{constructor(e){this.container=e}async init(e){const t=this.container,i=e.options.life;i&&(e.life={delay:t.retina.reduceFactor?(0,n.VG)(i.delay.value)*(i.delay.sync?1:(0,n.G0)())/t.retina.reduceFactor*n.Xu:0,delayTime:0,duration:t.retina.reduceFactor?(0,n.VG)(i.duration.value)*(i.duration.sync?1:(0,n.G0)())/t.retina.reduceFactor*n.Xu:0,time:0,count:i.count},e.life.duration<=0&&(e.life.duration=-1),e.life.count<=0&&(e.life.count=-1),e.life&&(e.spawning=e.life.delay>0),await Promise.resolve())}isEnabled(e){return!e.destroyed}loadOptions(e){e.life||(e.life=new o);for(var t=arguments.length,i=new Array(t>1?t-1:0),n=1;n<t;n++)i[n-1]=arguments[n];for(const s of i)e.life.load(null===s||void 0===s?void 0:s.life)}async update(e,t){if(!this.isEnabled(e)||!e.life)return;const{updateLife:n}=await i.e(6058).then(i.bind(i,6058));n(e,t,this.container.canvas.size)}}}}]);
//# sourceMappingURL=3089.86c1167b.chunk.js.f1dc575beac4.map