const inputs = document.querySelectorAll(".input");


function addcl(){
	let parent = this.parentNode.parentNode;
	parent.classList.add("focus");
}

function remcl(){
	let parent = this.parentNode.parentNode;
	if(this.value == ""){
		parent.classList.remove("focus");
	}
}


inputs.forEach(input => {
	input.addEventListener("focus", addcl);
	input.addEventListener("blur", remcl);
});


console.log('Wait for nice message')
setTimeout(() => {
    console.log("are you still there")
}, 3000)

setTimeout(() => {
    console.log('realy!!!!')
}, 4000)

setTimeout(() => {
    console.log('I make fun of you')
}, 5000)
setTimeout(() => {
    console.log('here is the message')
}, 6000)

setTimeout(() => {
    console.log('Allah is very merciful')
},8000)