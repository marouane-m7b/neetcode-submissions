class Solution {
    /**
     * @param {string[]} words
     * @return {string[]}
     */
    commonChars(words) {
        let result = [];
        let firstWord = words[0];

        for (let i = 0; i < firstWord.length; i++) {
            let char = firstWord[i];
            let isCommon = true;

            for (let j = 1; j < words.length; j++) {
                if (words[j].includes(char)) {
                    words[j] = words[j].replace(char, "");
                } else {
                    isCommon = false;
                    break;
                }
            }

            if (isCommon) {
                result.push(char);
            }
        }

        return result;
    }
}
