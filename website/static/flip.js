function nextPic(){
//alert("test1")

var x = Math.floor((Math.random() * 2) + 1); //rng var to load a random arrow

if (x == 1) {
    document.getElementById("image").src = "static/images/coin_head.png"
} else if (x == 2) {
    document.getElementById("image").src = "static/images/coin_tail.png"
} else {
    document.getElementById("image").src = "static/images/question_mark.png"
}

}

function ButtonClick(answer){
    var img = document.getElementById("image"); //variable used to check the arrow image
    var count = parseInt(document.getElementById("counter").value);
    var counter_highest = parseInt(document.getElementById("counter_highest").value);
    var wins = parseInt(document.getElementById("wins").value);
    var loses = parseInt(document.getElementById("loses").value);


    //if loop to see if the users input from the button matches the actual direction of the image arrow using 'indexOf' to check the file name
    if(answer == 'heads' && img.src.indexOf('static/images/coin_head.png') > -1){
        count++;
        wins++;
        document.getElementById("result").innerHTML = 'Correct!';
        document.getElementById("counter").value = count;
        document.getElementById("wins").value = wins;
    } else if (answer == 'tails' && img.src.indexOf('static/images/coin_tail.png') > -1) {
        count++;
        wins++;
        document.getElementById("result").innerHTML = 'Correct!';
        document.getElementById("counter").value = count;
        document.getElementById("wins").value = wins;
    } else {
        count = 0;
        loses++;
        document.getElementById("result").innerHTML = 'Wrong!';
        document.getElementById("counter").value = count;
        document.getElementById("loses").value = loses;
    }

    if(count > counter_highest){
        document.getElementById("counter_highest").value = count;
    }
}