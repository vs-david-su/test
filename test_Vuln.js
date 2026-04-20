// test_vuln.js
function runCode(userInput) {
    // 這是經典的程式碼注入漏洞
    // ESLint 規則：no-eval
    var result = eval(userInput);
    console.log(result);
}
// test
runCode("alert('hacked')");