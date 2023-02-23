const { SerialPort, ReadlineParser, SerialPortStream } = require("serialport");
// const readline = require("readline");
var prompt = require("prompt-sync")();

const parser = new ReadlineParser();

const port = new SerialPort({
  path: "COM5",
  baudRate: 9600,
  autoOpen: false,
});

port.pipe(parser);
parser.on("data", console.log);
try {
  port.open();
} catch (error) {
  console.log(error);
}
console.log("input d for door,\n",
			"w for window,\n",
			"l for lights,\n",
			"s for soild humidity info,\n",
			"q for quit")
while (true) {

  var n = prompt("Input ");
  console.log(n)
  port.write(n)
  if (n == "q") {
    break;
  }
}

/*
console.log("input d for door,\n",
			"w for window,\n",
			"l for lights,\n",
			"s for soild humidity info,\n",
			"q for quit")


do{
	var n = prompt("Input here please: ");
	//console.log(typeof n);
	if (n=="q"){
		break;
	}
	 writeHouse(n)
	
}while (true)

async function  writeHouse(n){
	port.write(n);
}
*/
