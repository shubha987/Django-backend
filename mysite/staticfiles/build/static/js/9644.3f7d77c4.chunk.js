"use strict";(self.webpackChunkparticles=self.webpackChunkparticles||[]).push([[9644],{9644:(o,a,i)=>{i.d(a,{OpacityUpdater:()=>e});var t=i(4409);class e{constructor(o){this.container=o}async init(o){const a=o.options.opacity;o.opacity=(0,t.Xs)(a,1);const i=a.animation;i.enable&&(o.opacity.velocity=(0,t.VG)(i.speed)/t.a5*this.container.retina.reduceFactor,i.sync||(o.opacity.velocity*=(0,t.G0)())),await Promise.resolve()}isEnabled(o){var a,i,t,e;return!o.destroyed&&!o.spawning&&!!o.opacity&&o.opacity.enable&&((null!==(a=o.opacity.maxLoops)&&void 0!==a?a:0)<=0||(null!==(i=o.opacity.maxLoops)&&void 0!==i?i:0)>0&&(null!==(t=o.opacity.loops)&&void 0!==t?t:0)<(null!==(e=o.opacity.maxLoops)&&void 0!==e?e:0))}reset(o){o.opacity&&(o.opacity.time=0,o.opacity.loops=0)}async update(o,a){this.isEnabled(o)&&o.opacity&&((0,t.UC)(o,o.opacity,!0,o.options.opacity.animation.destroy,a),await Promise.resolve())}}}}]);
//# sourceMappingURL=9644.3f7d77c4.chunk.js.map