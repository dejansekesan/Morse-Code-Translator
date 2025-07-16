#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char *morse_letters[] = {
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
    "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
    "..-", "...-", ".--", "-..-", "-.--", "--.."
};

char *morse_digits[] = {
    "-----", ".----", "..---", "...--", "....-", ".....",
    "-....", "--...", "---..", "----."
};

 /*/ void debug_print_end(const char *str) {
    size_t len = strlen(str);
    printf("DEBUG last chars in hex: ");
    for (size_t i = (len > 10 ? len - 10 : 0); i < len; i++) {
        printf("%02X ", (unsigned char)str[i]);
    }
    printf("\n");
} /*/
void fix_all_escape_sequences(char *str) {
    char *p = str;
    while ((p = strstr(p, "^[E")) != NULL) {
        size_t tail_len = strlen(p + 3);  // length of string from char after 'E' onwards

        // Shift tail right by 1 to make space for extra ' '
        memmove(p + 4, p + 3, tail_len + 1); // +1 for null terminator

        // Insert space after 'E'
        p[0] = ' ';
        p[1] = ' ';
        p[2] = '\n';
        p[3] = ' ';

        p += 4; // move pointer past inserted space to avoid infinite loop
    }
}





void text_to_morse(char *str) {
    FILE *output = fopen("output.txt", "w");
    if (!output) {
        perror("fopen");
        return;
    }

    fprintf(output, "Text to Morse Code Output:\n\n");

    for (int i = 0; str[i] != '\0'; i++) {
        unsigned char c = (unsigned char)str[i];

        if (c == 197 && (unsigned char)str[i + 1] == 161) { // š
            fprintf(output, "%s ", morse_letters['s' - 'a']);
            i++;
        }
        else if (c == 196 && (unsigned char)str[i + 1] == 135) { // ć
            fprintf(output, "%s ", morse_letters['c' - 'a']);
            i++;
        }
        else if (c == 196 && (unsigned char)str[i + 1] == 145) { // đ
            fprintf(output, "%s %s ", morse_letters['d' - 'a'], morse_letters['j' - 'a']); // dj
            i++;
        }
        else if (c == 196 && (unsigned char)str[i + 1] == 141) { // č
            fprintf(output, "%s ", morse_letters['c' - 'a']);
            i++;
        }
        if (c == 197 && (unsigned char)str[i+1] == 160) { // Š uppercase
            fprintf(output, "%s ", morse_letters['s' - 'a']);  // same as lowercase š
            i++; // skip second byte
        }
        else if (c == 196 && (unsigned char)str[i+1] == 144) { // Đ uppercase
            fprintf(output, "%s %s ", morse_letters['d' - 'a'], morse_letters['j' - 'a']); // dj
            i++;
        }
        else if (c == 196 && (unsigned char)str[i+1] == 134) { // Ć uppercase
            fprintf(output, "%s ", morse_letters['c' - 'a']);
            i++;
        }
        else if (c == 196 && (unsigned char)str[i+1] == 140) { // Č uppercase
            fprintf(output, "%s ", morse_letters['c' - 'a']);
            i++;
        }
        else if ((unsigned char)str[i] == 27 && str[i + 1] == 'E') { // ESC + E
            fprintf(output, "\n");
            i++;
            continue;
        }
        else if (str[i] >= 'A' && str[i] <= 'Z') {
            fprintf(output, "%s ", morse_letters[str[i] - 'A']);
        }
        else if (str[i] >= 'a' && str[i] <= 'z') {
            fprintf(output, "%s ", morse_letters[str[i] - 'a']);
        }
        else if (str[i] >= '0' && str[i] <= '9') {
            fprintf(output, "%s ", morse_digits[str[i] - '0']);
        }
        else if (str[i] == ',') {
            fprintf(output, ", ");
        }
        else if (str[i] == '?') {
            fprintf(output, "? ");
        }
        else if (str[i] == '!') {
            fprintf(output, "! ");
        }
        else if (str[i] == ' ') {
            fprintf(output, "/ ");
        }
        else if (str[i] == '.') {
            fprintf(output, "// ");
        }
        else if (str[i] == ')') {
            fprintf(output, ") ");
        }
        else if (str[i] == '(') {
            fprintf(output, "( ");
        }
        else if (str[i] == '"') {
            fprintf(output, "\" ");
        }
        else if (str[i] == '-') {
            fprintf(output,"-....- ");
        }
        else if (str[i] == '\'') {
            fprintf(output, "' ");
        }
        else if (str[i] == ':') {
            fprintf(output, ": ");
        }
        else if (str[i] == ';') {
            fprintf(output, "; ");
        }
        else if (str[i] == '\n') {
            fprintf(output, "\n");
        }
        else if (str[i] == '#') {
            fprintf(output, "# ");
        }
        
    }

    fprintf(output, "\n");
    fclose(output);
}



void morse_to_text(char *morse_input) {
    FILE *output = fopen("output.txt", "w");
    if (!output) {
        perror("fopen");
        return;
    }

    fprintf(output, "Morse Code to Text Output:\n\n");

    char *p = morse_input;
    while (*p) {
        // Skip spaces
        if (*p == ' ') {
            p++;
            continue;
        }

        // Handle newline
        if (*p == '\n') {
            fprintf(output, "\n");
            p++;
            continue;
        }

        // Extract token until next space or newline
        char token[32] = {0};  // Morse code is short
        int i = 0;
        while (*p && *p != ' ' && *p != '\n' && i < 31) {
            token[i++] = *p++;
        }
        token[i] = '\0';

        int found = 0;

        // Check for letters
        for (int j = 0; j < 26; j++) {
            if (strcmp(token, morse_letters[j]) == 0) {
                fprintf(output, "%c", 'A' + j);
                found = 1;
                break;
            }
        }

        // Check for digits
        if (!found) {
            for (int j = 0; j < 10; j++) {
                if (strcmp(token, morse_digits[j]) == 0) {
                    fprintf(output, "%c", '0' + j);
                    found = 1;
                    break;
                }
            }
        }

        // Check for punctuation
        if (!found) {
            if (strcmp(token, ",") == 0) fprintf(output, ","), found = 1;
            else if (strcmp(token, "?") == 0) fprintf(output, "?"), found = 1;
            else if (strcmp(token, "!") == 0) fprintf(output, "!"), found = 1;
            else if (strcmp(token, "\"") == 0) fprintf(output, "\""), found = 1;
            else if (strcmp(token, "//") == 0) fprintf(output, "."), found = 1;
            else if (strcmp(token, ")") == 0) fprintf(output, ")"), found = 1;
            else if (strcmp(token, "(") == 0) fprintf(output, "("), found = 1;
            else if (strcmp(token, "-....-") == 0) fprintf(output, "-"), found = 1;
            else if (strcmp(token, "'") == 0) fprintf(output, "'"), found = 1;
            else if (strcmp(token, ":") == 0) fprintf(output, ":"), found = 1;
            else if (strcmp(token, ";") == 0) fprintf(output, ";"), found = 1;
            else if (strcmp(token, "/") == 0) fprintf(output, " "), found = 1;
            else if (strcmp(token, "#") == 0) fprintf(output, "#"), found = 1;
        }

        if (!found) {
            fprintf(output, "?");
        }
    }

    fclose(output);
}



// helper function to read full file into heap buffer
char *read_file(const char *filename) {
    FILE *f = fopen(filename, "rb");
    if (!f) {
        perror("fopen");
        exit(1);
    }

    fseek(f, 0, SEEK_END);
    long size = ftell(f);
    rewind(f);

    char *buffer = malloc(size + 1);
    if (!buffer) {
        perror("malloc");
        fclose(f);
        exit(1);
    }

    fread(buffer, 1, size, f);
    buffer[size] = '\0';
    fclose(f);
    return buffer;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <1=text_to_morse | 2=morse_to_text>\n", argv[0]);
        return 1;
    }

    char *input = read_file("input.txt");

    FILE *out = fopen("output.txt", "w");
    if (!out) {
        perror("fopen output.txt");
        free(input);
        return 1;
    }

    if (argv[1][0] == '1') {
        // redirect stdout to file
        FILE *original_stdout = stdout;
        stdout = out;

        text_to_morse(input);

        stdout = original_stdout;
    } else if (argv[1][0] == '2') {
        fix_all_escape_sequences(input);

        FILE *original_stdout = stdout;
        stdout = out;

        morse_to_text(input);

        stdout = original_stdout;
    } else {
        fprintf(stderr, "Invalid mode.\n");
        fclose(out);
        free(input);
        return 1;
    }

    fclose(out);
    free(input);
    return 0;
}