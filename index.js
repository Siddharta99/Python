var guestList = ["Vishal","Arjun","Anuja","Raj","Pranjal"];

function whosPaying(guestList){

    var numberOfPeople = guestList.length;
    var i = Math.floor(Math.random()*numberOfPeople); //0-0.9999  /0-4.9999

    var guestName = guestList[i];

    return guestName + " is going to buy lunch today!"
}