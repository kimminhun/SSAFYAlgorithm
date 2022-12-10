function solution(numbers, k) {
    const stack = []
    let answer = '';
    for( let i = 0; i < numbers.length; i++){
        const v = numbers[i];

        while(k>0 && stack[stack.length-1] < v){
            stack.pop();
            k -= 1

        }

        stack.push(v);
    }
        stack.splice(stack.length -k, k);
        answer = stack.join('');
        return answer;
    
}