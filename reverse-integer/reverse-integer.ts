function reverse(x: number): number {
    let y = '';
    const MIN = -2147483648;
    const MAX = 2147483647;
    let isNegative = x < 0;
    
    while (x !== 0) {
        y += Math.abs(x % 10);
        x = Math.trunc(x / 10);
    }

    let result = Number(y);
    if (isNegative) result = result * -1;

    if (result < MIN || result > MAX) {
        return 0;
    }

    return result;
}