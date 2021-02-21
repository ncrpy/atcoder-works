#include <stdio.h>

int main(void) {
    char S[1001];
    scanf("%s", S);

    char *ans = "Yes";
    for (int i = 0; S[i] != '\0'; i++) {
        if ((i % 2 == 0) && 'A' <= S[i] && S[i] <= 'Z') {
            ans = "No";
        } else if ((i % 2 == 1) && 'a' <= S[i] && S[i] <= 'z') {
            ans = "No";
        } else {
            continue;
        }
        break;
    }
    printf("%s\n", ans);
}
