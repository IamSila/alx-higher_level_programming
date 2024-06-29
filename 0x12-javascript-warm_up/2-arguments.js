#!/usr/bin/node
let arguments = process.argv.slice(2);
console.log("Number of arguments", arguments.length);


if (arguments.length === 0){
	console.log('No argument');
}

else if (arguments.length === 1){
	console.log('Argument found');
}

else{
	console.log("Aguments found");
}
