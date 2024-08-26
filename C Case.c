#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#define Admin_USM "RJ"
#define Admin_Pass "Rohan@2266"
#define MAX 100

typedef struct {
    char username[100];
    char password[100];
    char address[100];
    char email[100];
    char age[100];
} User;

typedef struct {
    char products[100];
    char quantity[100];
    char price[100];
} Product;

User users[MAX];
Product prod[MAX];
int num_users = 0;
int num_pds = 0;

void load_data() {
    FILE *fr = fopen("user.csv", "r");
    char line[1000];

    if (fr == NULL) {
        printf("Error in opening the file\n");
        return;
    }

    while (fgets(line, sizeof(line), fr) != NULL) {
        char *token = strtok(line, ",");
        if (token != NULL) strcpy(users[num_users].username, token);

        token = strtok(NULL, ",");
        if (token != NULL) strcpy(users[num_users].password, token);

        token = strtok(NULL, ",");
        if (token != NULL) strcpy(users[num_users].address, token);

        token = strtok(NULL, ",");
        if (token != NULL) strcpy(users[num_users].email, token);

        token = strtok(NULL, ",");
        if (token != NULL) strcpy(users[num_users].age, token);

        token = strtok(NULL, ",");
        if (token != NULL) strcpy(prod[num_pds].products, token);

        token = strtok(NULL, ",");
        if (token != NULL) strcpy(prod[num_pds].quantity, token);

        token = strtok(NULL, ",");
        if (token != NULL) strcpy(prod[num_pds].price, token);

        num_users++;
        num_pds++;
    }

    fclose(fr);
}

void save_data() {
    FILE *fw = fopen("user.csv", "w");

    if (fw == NULL) {
        printf("Error in opening the file\n");
        return;
    }

    for (int i = 0; i < num_users; i++) {
        fprintf(fw, "%s,%s,%s,%s,%s\n", users[i].username, users[i].password, users[i].address, users[i].email, users[i].age);
    }

    for (int i = 0; i < num_pds; i++) {
        fprintf(fw, "%s,%s,%s\n", prod[i].products, prod[i].quantity, prod[i].price);
    }

    fclose(fw);
}

void admin(int num_users) {
    int n;
    while (1) {
        printf("1: See the users in database\n2: Data Update\n3: View database\n4: Exit\n");
        printf("Enter the choice\n");
        scanf("%d", &n);
        if (n == 1) {
            printf("Username \t Age \t Email \t Address\n");
            for (int i = 0; i < num_users; i++) {
                printf("%s \t %s \t %s \t %s\n", users[i].username, users[i].age, users[i].email, users[i].address);
            }
        }
        else if (n == 2) {
            char pod[100];
            printf("Enter product name: ");
            scanf("%s", pod);
            for (int i = 0; i < num_pds; i++) {
                if (strcmp(pod, prod[i].products) == 0) {
                    printf("Product exists\n");
                    printf("%s \t %s\n", prod[i].quantity, prod[i].price);
                    printf("Enter new quantity: ");
                    scanf("%s", prod[i].quantity);
                    printf("Enter new price: ");
                    scanf("%s", prod[i].price);
                    save_data();
                    return;
                }
            }
        }
        else if (n == 3) {
            printf("Product \t Price \t Quantity\n");
            for (int j = 0; j < num_pds; j++) {
                printf("%s \t %s \t %s\n", prod[j].products, prod[j].price, prod[j].quantity);
            }
        }
        else if (n == 4) {
            break;
        }
    }
}

void home(int c) {
    while (1) {
        printf("Please select an option\n");
        printf("1: Product\n2: Cart\n3: Profile\n4: Exit\n");
        int n;
        scanf("%d", &n);
        if (n == 1) {
            char s[100];
            printf("Product Catalogue\n");
            for (int j = 0; j < num_pds; j++) {
                printf("%s \t %s\n", prod[j].products, prod[j].quantity);
            }
            printf("Search product: ");
            scanf("%s", s);
            for (int i = 0; i < num_pds; i++) {
                if (strstr(prod[i].products, s) != NULL) {
                    printf("%s \t %s\n", prod[i].products, prod[i].price);
                }
            }
        }
        else if (n == 2) {
            // Cart functionality not implemented
            break;
        }
        else if (n == 3) {
            printf("Profile\n");
            printf("USN: %d\n", c);
            printf("Name: %s\n", users[c].username);
            printf("Age: %s\n", users[c].age);
            printf("Email: %s\n", users[c].email);
            printf("Address: %s\n", users[c].address);
            break;
        }
        else if (n == 4) {
            break;
        }
    }
}

void user_signup() {
    char username[100];
    char password[100];
    char address[100];
    char age[100];
    char email[100];
    printf("Enter the username: ");
    scanf("%s", username);
    for (int i = 0; i < num_users; i++) {
        if (strcmp(users[i].username, username) == 0) {
            printf("Username is already taken. Please try again.\n");
            return;
        }
    }

    printf("Enter the password: ");
    scanf("%s", password);
    printf("Enter the address: ");
    scanf("%s", address);
    printf("Enter the email: ");
    scanf("%s", email);
    printf("Enter the age: ");
    scanf("%s", age);

    strcpy(users[num_users].username, username);
    strcpy(users[num_users].password, password);
    strcpy(users[num_users].address, address);
    strcpy(users[num_users].email, email);
    strcpy(users[num_users].age, age);

    printf("Account created successfully. Your USN is %d\n", num_users);
    num_users++;

    FILE *fw = fopen("user.csv", "a");
    if (fw == NULL) {
        printf("Error in opening the file\n");
        return;
    }

    fprintf(fw, "%s,%s,%s,%s,%s\n", username, password, address, email, age);
    fclose(fw);
}

void user_login() {
    char usn[50];
    char pass[50];
    int c;
    printf("Enter the username: ");
    scanf("%s", usn);

    if (strcmp(Admin_USM, usn) == 0) {
        printf("Enter the password: ");
        scanf("%s", pass);
        if (strcmp(Admin_Pass, pass) == 0) {
            printf("Welcome, Admin\n");
            admin(num_users);
        } else {
            printf("Incorrect password\n");
        }
        return;
    }

    for (int i = 0; i < num_users; i++) {
        if (strcmp(users[i].username, usn) == 0) {
            printf("Enter the password: ");
            scanf("%s", pass);
            if (strcmp(users[i].password, pass) == 0) {
                printf("Welcome back, %s\n", users[i].username);
                home(i);
            } else {
                printf("Incorrect password\n");
            }
            return;
        }
    }

    printf("Invalid username\n");
}

int main() {
    load_data();

    int choice;
    while (1) {
        printf("Welcome to E-Shop\n");
        printf("Please select an option:\n1: Signup\n2: Login\n3: Exit\n");
        scanf("%d", &choice);

        if (choice == 1) {
            user_signup();
        } else if (choice == 2) {
            user_login();
        } else if (choice == 3) {
            printf("Thank you for visiting\n");
            break;
        } else {
            printf("Invalid choice\n");
        }
    }

    return 0;
}
