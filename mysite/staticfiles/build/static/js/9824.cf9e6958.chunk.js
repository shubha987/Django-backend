"use strict";(self.webpackChunkparticles=self.webpackChunkparticles||[]).push([[9824],{9824:(s,o,e)=>{e.d(o,{absorb:()=>n});var i=e(4409);const t=.5,a=10,d=0;function c(s,o,e,c,n,u){const r=(0,i.qE)(s.options.collisions.absorb.speed*n.factor/a,d,c);s.size.value+=r*t,e.size.value-=r,c<=u&&(e.size.value=0,e.destroy())}function n(s,o,e,i){const t=s.getRadius(),a=o.getRadius();void 0===t&&void 0!==a?s.destroy():void 0!==t&&void 0===a?o.destroy():void 0!==t&&void 0!==a&&(t>=a?c(s,0,o,a,e,i):c(o,0,s,t,e,i))}}}]);
//# sourceMappingURL=9824.cf9e6958.chunk.js.map