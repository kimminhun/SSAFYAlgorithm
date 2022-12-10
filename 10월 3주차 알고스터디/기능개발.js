function solution(progresses, speeds) {
    var answer = [];
    let days = progresses.map((progress, index) => Math.ceil((100 - progress) / speeds[index]));
    while(days.length){
        const a = days.shift();
        let ans = 1; //출시일
        function dep(){
        return (days[0] <= a) ? (ans += 1 , days.shift() , dep()) : (answer.push(ans) , ans = 1)
        }
        dep()
    }
    return answer;
}