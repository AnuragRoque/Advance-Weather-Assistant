let select = s => document.querySelector(s),
  selectAll = s =>  document.querySelectorAll(s),
		mainSVG = select('#mainSVG')

gsap.set('svg', {
	visibility: 'visible'
})

let tl = gsap.timeline();
tl.to('.smallBlob', {
	x: 157,
	attr:{
		r: (count) => {
			console.log(count)
			return (count == 3) ? 53 : 0
		}
	},
	stagger: {
		each: 0.05
	},
	ease: 'power4.inOut'
})
.to('.mainBlob', {
	attr: {
		r: 0
	},
	x: 80,
	ease: 'sine.inOut'
}, 0)
.from('.bigBlob', {
	attr: {
		r: 0
	},
	x: -80,
	//ease: 'elastic(0.4, 0.7)'
	ease: 'power2.inOut'
}, 0)

.to('.bigBlob', {
	fill: '#65E04D',
	ease: 'power2.inOut'
}, 0)

.to('.buttonInnerShadowFlood', {
	floodColor: '#D1F367',
	ease: 'power2.inOut'
}, 0)
.to('.buttonInnerShadow2Flood', {
	floodColor: '#07AA22',
	ease: 'power2.inOut'
}, 0)

.to('.buttonDropShadowFlood', {
	floodColor: '#39AC4F',
	ease: 'power2.inOut'
}, 0).timeScale(1.6)


let isOn = true;
mainSVG.onclick = (e) => {
	isOn = !isOn;
	
	if(isOn) {
		tl.play();
	} else {
		tl.reverse()
	}
}
//ScrubGSAPTimeline(tl)