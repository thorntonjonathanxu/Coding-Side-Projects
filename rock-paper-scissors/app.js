//Global Variables
let userScore = 0;
let compScore = 0;

//Cacheing Dom Variables that store the HTML elements, use this to update HTML Doc on updates
const userScore_span = document.getElementById("user-score");
const compScore_span = document.getElementById("computer-score");
const scoreBoard_div = document.querySelector(".score-board");
const result_div = document.querySelector(".result > p");
const rock_div = document.getElementById("rock");
const paper_div = document.getElementById("paper");
const scissors_div = document.getElementById("scissors");

function getComputerChoice(){
    const choices = ['rock','paper','scissors']
    return choices[Math.floor(Math.random() * 3 )];
}

function toUppercase(string){
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function win(userChoice, computerChoise){
    
    userScore++;
    userScore_span.innerHTML = userScore;
    result_div.innerHTML = `${toUppercase(userChoice)} beats ${toUppercase(computerChoise)}. You win!`;
    const userChoice_div = document.getElementById(userChoice);
    userChoice_div.classList.add('green-glow');
    setTimeout(() => userChoice_div.classList.remove('green-glow'), 500);
}
function lose(userChoice,computerChoise){
    const userChoice_div = document.getElementById(userChoice);
    compScore++;
    compScore_span.innerHTML = compScore;
    result_div.innerHTML = `${toUppercase(userChoice)} loses to ${toUppercase(computerChoise)}. You lose!`;
    userChoice_div.classList.add('red-glow');
    setTimeout(() => userChoice_div.classList.remove('red-glow'), 500);
}
function draw(userChoice,computerChoise){
    const userChoice_div = document.getElementById(userChoice);
    result_div.innerHTML = `${toUppercase(userChoice)} matches ${toUppercase(computerChoise)}. Its a draw!`;
    userChoice_div.classList.add('gray-glow');
    setTimeout(() => userChoice_div.classList.remove('gray-glow'), 500);
}
function game(userChoice){
    const computerChoise = getComputerChoice();
    switch(userChoice + computerChoise) {
        case 'rockscissors':
        case 'paperrock':
        case 'scissorspaper':
            win(userChoice,computerChoise);
            break;
        case 'rockpaper':
        case 'paperscissors':
        case 'scissorsrock':
            lose(userChoice,computerChoise);
            break;
        case 'rockrock':
        case 'paperpaper':
        case 'scissorsscissors':
            draw(userChoice,computerChoise);
            break;
    }
}

function main() {
    rock_div.addEventListener('click', function(){
        game("rock");
    })
    paper_div.addEventListener('click', function(){
        game("paper");
    })
    scissors_div.addEventListener('click', function(){
        game("scissors");
    })
}
main();
