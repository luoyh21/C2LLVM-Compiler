#include <stdio.h>
#include <string.h>

int main()
{
    char input_str[1000];
    int count = 0;
    int numbers[5000];

    printf("Please input Char Array Under 1000 characters\n");
    gets(input_str);

    int len = strlen(input_str);
    int temp = 0;

    for (int i = len - 1; i >= 0; i = i - 1)
    {
        if (input_str[i] == ',')
        {
            numbers[count] = temp;
            temp = 0;
            count = count + 1;
        }
        else if (input_str[i] == '-')
        {
            temp = 0 - temp;
        }
        else
        {
            temp = temp * 10 + input_str[i] - '0';
        }
    }
    numbers[count] = temp;
    count = count + 1;

    // Bubble Sort
    for (int i = 0; i < count; i = i + 1)
    {
        for (int j = 0; j < count - i - 1; j = j + 1)
        {
            if (numbers[j] > numbers[j + 1])
            {
                int temp = numbers[j];
                numbers[j] = numbers[j + 1];
                numbers[j + 1] = temp;
            }
        }
    }

    // Print
    for (int i = 0; i < count - 1; i = i + 1)
    {
        printf("%d,", numbers[i]);
    }
    printf("%d\n", numbers[count - 1]);
}