///*
//1001
//#include <stdio.h>
//int main()
//{
//    printf("Hello world!\n");
//}
//*/
///*
//#include <stdio.h>
//int main()
//{
//    // 정수, 문자, 실수, 문자열
//    int a;
//    scanf("%d",&a);
//    printf("%d",a);
//
//}
//*/
///*
//#include <stdio.h>
//int main()
//{
//    char a;
//    scanf("%c", &a);
//    printf("%c",a);
//}
//*/
////#include <stdio.h>
////int main()
////{
////    double a;
////    scanf("%lf", &a);
////    printf("%.2lf",a);
////}
//
////#include <stdio.h>
////int main()
////{
////    int a,b;
////    scanf("%d %d", &a, &b);
////    if(a>b){
////        printf(">");
////    }else if(a<b){
////    printf("<");
////    }else{
////        printf("=");
////    }
////}
////#include <stdio.h>
////int main()
////{
////    int a;
////    scanf("%d",&a);
////    if(a==1|| a==3 || a==5 || a==7){
////        printf("oh my god");
////    }else{
////        printf("enjoy");
////    }
////}
////#include <stdio.h>
////int main()
////{
////    int a,c;
////    char b;
////    scanf("%d%c%d", &a,&b,&c);
////    if (b =='+'){
////        printf("%d" , a+c);
////    }else if(b == '-'){
////        printf("%d", a-c);
////    }else if (b == '*'){
////        printf("%d",a*c);
////    }else{
////        printf("%.2lf",(double)a/c);
////    }
////
////}
////#include <stdio.h>
////int main()
////{
////   int a, i;
////   scanf("%d", &a);
////   for (i=1; i<=a; i++){
////    printf("%d ",i);
////   }
////}
////#include <stdio.h>
////int main()
////{
////    char a, b, i;
////    scanf("%c %c", &a, &b);
////    for(i=a;i<=b; i++){
////        printf("%c ", i);
////    }
////}
//
////#include <stdio.h>
////int main()
////{
////    int a,b,i;
////    scanf("%d %d", &a, &b);
////    for (i=a;i<=b;i++){
////        if(i%2==1){
////            printf("%d ", i);
////        }
////    }
////}
//
////#include <stdio.h>
////int main()
////{
////   int a, i;
////   scanf("%d", &a);
////   for(i=1;i<=9;i++){
////      printf("%d*%d=%d\n",a,i,a*i);
////   }
////}
////#include <stdio.h>
////int main()
////{
////    int a,i,b;
////    int sum = 0;
////    scanf("%d",&a);
////    for(i=1;i<=a;i++){
////        scanf("%d",&b);
////        sum=sum+b;
////    }
////    printf("%d", sum);
////}
////#include <stdio.h>
////int main()
////{
////    int a,i;
////    scanf("%d",&a);
////    for(i=a;i>=1;i--){
////        printf("%d\n", i);
////    }
//////}
////#include <stdio.h>
////int main()
////{
////    int a,i,j;
////    scanf("%d", &a);
////    for(i=1;i<=a;i++){ //세로반복
////        for(j=1;j<=i;j++){ //가로반복
////            printf("*");
////        }
////        printf("\n"); // 줄바꾸기
////    }
////}
////1351
////#include <stdio.h>
////int main()
////{
////    int a,b,i,j;
////    scanf("%d %d",&a,&b);
////    for(i=a;i<=b;i++){
////        for(j=1;j<=9;j++){
////            printf("%d*%d=%d\n",i,j,i*j);
////        }
////    }
////}
////1403
////#include <stdio.h>
////int main()
////{
////    int a, i;
////    scanf("%d",&a);
////    int arr[a];
////    for(i=0; i<a; i++){
////        scanf("%d",&arr[i]);
////    }
////    for(i=0; i<a; i++){
////        printf("%d\n",arr[i]);
////    }
////    for(i=0; i<a; i++){
////        printf("%d\n",arr[i]);
////    }
////
////
////}
////#include <stdio.h>
////int main()
////{
////    int a, i;
////    int *p;
////    scanf("%d",&a);
////    int arr[a];
////    p = arr; //&arr[0]
////    for(i=0; i<a; i++){
////        scanf("%d",p+i);
////    }
////    for(i=0; i<a; i++){
////        printf("%d\n",*(p+i));
////    }
////    for(i=0; i<a; i++){
////        printf("%d\n",*(p+i));
////    }
////}
////4561
//#include <stdio.h>
//int main()
//{
//    int arr[7];
//    int a, i;
//    int sum = 0;
//    int min=100;
//    int *p;
//
//    for(i=0;i<7; i++){
//        scanf("%d", &arr[i]);
//    }
//    p=arr;
//    for(i=0;i<7;i++){
//        if(*(p+i)%2==1){
//            sum=sum+*(p+i);
//            if(*(p+i)<min){
//                min =*(p+i);
//            }
//        }
//    }
//    if(sum==0){
//        printf("-1");
//    }else{
//        printf("%d\n",sum);
//        printf("%d",min);
//    }
//}
////4891
//#include <stdio.h>
//int main()
//{
//    int a, i;
//    scanf("%d", &a);
//    int arr[a];
//    int* p =arr;
//    int min=1000, max=0;
//
//    for(i=0; i<a; i++){
//        scanf("%d", &arr[i]);
//    }
//
//    for(i=0;i<a;i++){
//        if(*(p+i)>max){
//            max=*(p+i);
//        }
//        if(*(p+i)<min){
//            min=*(p+i);
//        }
//    }
//    printf("%d",max-min);
//}
//#include <stdio.h>
//#include <malloc.h>
//int main()
//{
//    int a, i;
//    scanf("%d", &a);
//    int arr[a];
//    int* p =(int*)malloc(sizeof(int)*a);
//    int min=1000, max=0;
//
//    for(i=0; i<a; i++){
//        scanf("%d", p+i);
//    }
//
//    for(i=0;i<a;i++){
//        if(*(p+i)>max){
//            max=*(p+i);
//        }
//        if(*(p+i)<min){
//            min=*(p+i);
//        }
//    }
//    printf("%d",max-min);
//    free(p);
//}
//1410
//#include <stdio.h>
//#include <string.h>
//int main()
//{
//    char arr[1000001];
//    int i, len;
//    int open=0, close=0;
//    scanf("%s",arr);
//    len =strlen(arr);
//    for(i=0;i<len;i++){
//        if(arr[i] == '('){
//            open++;
//           }else{
//            close++;
//           }
//    }
//    printf("%d %d", open, close);
//}
//5079
//#include <stdio.h>
//#include <string.h>
//int main()
//{
//    int a, i;
//    int _a=0, _b=0;
//    scanf("%d", &a);
//    char arr[a+1];
//    scanf("%s",arr);
//    for(i=0;i<a;i++){
//        if(arr[i] == 'A'){
//            _a++;
//        }else if(arr[i] == 'B'){
//            _b++;
//        }
//    }
//    if(_a>_b){
//        printf("A");
//    }else if(_a<_b){
//        printf("B");
//    }else{
//        printf("Tie");
//    }
//
//}
//1408
//#include <stdio.h>
//#include <string.h>
//int main()
//{
//    char arr[21];
//    int i, len;
//    scanf("%s",arr);
//    len = strlen(arr);
//    for(i=0; i<len; i++){
//        printf("%c", arr[i]+2);
//    }
//    printf("\n");
//
//    for(i=0; i<len; i++){
//        printf("%c", (arr[i]*7)%80+48);
//    }
//}
//1295
//#include <stdio.h>
//#include <string.h>
//#include <ctype.h>
//int main()
//{
//    char arr[1001];
//    int i, len;
//    scanf("%s", arr);
//    len = strlen(arr);
//    for(i=0;i<len;i++){
//        if(islower(arr[i])){
//            printf("%c", toupper(arr[i]));
//        }else if(isupper(arr[i])){
//                 printf("%c",tolower(arr[i]));
//        }else{
//            printf("%c",arr[i]);
//        }
//    }
//}
//4771
////1500
//#include <stdio.h>
//#include <string.h>
//#include <ctype.h>
//int main()
//{
//    int a, b, i, j;
//    scanf("%d %d", &a, &b);
//    int arr[a][b];
//
//    for(i=0; i<a; i++){
//        for(j=0; j<b; j++){
//            scanf("%d", &arr[i][j]);
//        }
//    }
//    for(i=0; i<a; i++){
//        for(j=0; j<b; j++){
//            printf("%d ", arr[i][j]);
//        }
//        printf("\n");
//    }
//}

//1096
//#include <stdio.h>
//#include <string.h>
//#include <ctype.h>
//int main()
//{
//    int arr[19][19] = {0};
//    int i, j;
//    int a,b,c;
//
//    scanf("%d", &a);
//    for(i=0;i<a;i++){
//        scanf("%d %d", &, &c);
//        arr[b-1][c-1] = 1;
//    }
//    for(i=0; i<19; i++){
//        for(j=0; j<19; j++){
//            printf("%d ", arr[i][j]);
//        }
//        printf("\n");
//    }
//}
////1402
//#include <stdio.h>
//#include <string.h>
//#include <ctype.h>
//int main()
//{
//    int a, i;
//    scanf("%d", &a);
//    int arr[a];
//    for(i=0; i<a;i++){
//        scanf("%d", &arr[i]);
//    }
//    for(i=a-1;i>=0; i--){
//        printf("%d ", arr[i]);
//    }
//}
//1660
//#include <stdio.h>
//#include <string.h>
//#include <ctype.h>
//int main()
//{
//   char arr[101];
//   int i, len;
//   scanf("%s", arr);
//   len = strlen(arr);
//   for(i=0;i<len; i++){
//    if(arr[i] == ','){
//        printf(" ");
//    }else{
//        printf("%c", arr[i]);
//    }
////   }
////}
////동적 할당
//#include <stdio.h>
//#include <string.h>
//#include <ctype.h>
//#include <malloc.h>
//int main()
//{
//   char *p = (char *)malloc(sizeof(char)*101);
//   int i, len;
//   scanf("%s", p);
//   len = strlen(p);
//   for(i=0;i<len; i++){
//    if(*(p+i) == ','){
//        printf(" ");
//    }else{
//        printf("%c", *(p+i));
//    }
//   }
//   free(p);
//}
//1674
//#include <stdio.h>
//#include <string.h>
//#include <ctype.h>
//#include <malloc.h>
//int main()
//{
//    int sum=0, i;
//    for(i=1; i<=10; i++){
//        scanf("%1d", &a);
//        sum = sum + a;
//    }
//    if(sum%7==4){
//        printf("Bad");
//    }else{
//        printf("Good");
//    }
//}
//1707
//#include <stdio.h>
//#include <string.h>

//int main()
//{
//    int arr[10];
//    int sum=0;
//    int i, big=0, small = 0;
//    double avg;
//
//    for(i=0;i<10; i++){
//        scanf("%d", &arr[i]);
//        sum = sum + arr[i];
//    }
//    avg = (double)sum/10;
//    printf("%.1lf\n", avg);
//
//    for(i=0; i<10; i++){
//        if(arr[i] >= avg){
//            big++;
//        }else{
//            small++;
//        }
//    }
//    printf("%d %d", big, small);
//}
//2081
//#include <stdio.h>
//#include <string.h>
//
//int main()
//{
//    int max=0;
//    int pos, a, i;
//    for(i=1; i<=9; i++){
//        scanf("%d", &a);
//        if(a>max){
//            max = a;
//            pos = i;
//        }
//    }
//    printf("%d\n",max);
//    printf("%d",pos);
//}
