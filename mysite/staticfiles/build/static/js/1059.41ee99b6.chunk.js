"use strict";(self.webpackChunkparticles=self.webpackChunkparticles||[]).push([[1059,4845],{4845:(e,i,o)=>{o.d(i,{bounce:()=>t});var s=o(4409);const d=e=>{void 0===e.collisionMaxSpeed&&(e.collisionMaxSpeed=(0,s.VG)(e.options.collisions.maxSpeed)),e.velocity.length>e.collisionMaxSpeed&&(e.velocity.length=e.collisionMaxSpeed)};function t(e,i){(0,s.pE)((0,s.Tg)(e),(0,s.Tg)(i)),d(e),d(i)}},1059:(e,i,o)=>{o.d(i,{destroy:()=>d});var s=o(4845);function d(e,i){if(e.unbreakable||i.unbreakable||(0,s.bounce)(e,i),void 0===e.getRadius()&&void 0!==i.getRadius())e.destroy();else if(void 0!==e.getRadius()&&void 0===i.getRadius())i.destroy();else if(void 0!==e.getRadius()&&void 0!==i.getRadius()){(e.getRadius()>=i.getRadius()?i:e).destroy()}}}}]);
//# sourceMappingURL=1059.41ee99b6.chunk.js.map