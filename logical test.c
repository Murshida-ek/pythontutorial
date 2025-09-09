# include <stdio.h>
# include <string.h>
int main()
{
    char str[100];
    int i, len, string = 1;
    printf("Enter a string: ");
    scanf("%s", str);
    len = strlen(str);
    for (i = 0; i < len / 2; i++) 
    {
        if (str[i] != str[len - i - 1]) {
            string= 0;
            break;
        }
    }

    if (string)
        printf("Palindrome\n");
    else
        printf("Not Palindrome\n");

    return 0;
}

