/*
1001
#include <stdio.h>
int main()
{
    printf("Hello world!\n");
}
*/
/*
#include <stdio.h>
int main()
{
    // 정수, 문자, 실수, 문자열
    int a;
    scanf("%d",&a);
    printf("%d",a);

}
*/
/*
#include <stdio.h>
int main()
{
    char a;
    scanf("%c", &a);
    printf("%c",a);
}
*/
//#include <stdio.h>
//int main()
//{
//    double a;
//    scanf("%lf", &a);
//    printf("%.2lf",a);
//}

//#include <stdio.h>
//int main()
//{
//    int a,b;
//    scanf("%d %d", &a, &b);
//    if(a>b){
//        printf(">");
//    }else if(a<b){
//    printf("<");
//    }else{
//        printf("=");
//    }
//}
//#include <stdio.h>
//int main()
//{
//    int a;
//    scanf("%d",&a);
//    if(a==1|| a==3 || a==5 || a==7){
//        printf("oh my god");
//    }else{
//        printf("enjoy");
//    }
//}
//#include <stdio.h>
//int main()
//{
//    int a,c;
//    char b;
//    scanf("%d%c%d", &a,&b,&c);
//    if (b =='+'){
//        printf("%d" , a+c);
//    }else if(b == '-'){
//        printf("%d", a-c);
//    }else if (b == '*'){
//        printf("%d",a*c);
//    }else{
//        printf("%.2lf",(double)a/c);
//    }
//
//}
//#include <stdio.h>
//int main()
//{
//   int a, i;
//   scanf("%d", &a);
//   for (i=1; i<=a; i++){
//    printf("%d ",i);
//   }
//}
//#include <stdio.h>
//int main()
//{
//    char a, b, i;
//    scanf("%c %c", &a, &b);
//    for(i=a;i<=b; i++){
//        printf("%c ", i);
//    }
//}

//#include <stdio.h>
//int main()
//{
//    int a,b,i;
//    scanf("%d %d", &a, &b);
//    for (i=a;i<=b;i++){
//        if(i%2==1){
//            printf("%d ", i);
//        }
//    }
//}

//#include <stdio.h>
//int main()
//{
//   int a, i;
//   scanf("%d", &a);
//   for(i=1;i<=9;i++){
//      printf("%d*%d=%d\n",a,i,a*i);
//   }
//}
//#include <stdio.h>
//int main()
//{
//    int a,i,b;
//    int sum = 0;
//    scanf("%d",&a);
//    for(i=1;i<=a;i++){
//        scanf("%d",&b);
//        sum=sum+b;
//    }
//    printf("%d", sum);
//}
//#include <stdio.h>
//int main()
//{
//    int a,i;
//    scanf("%d",&a);
//    for(i=a;i>=1;i--){
//        printf("%d\n", i);
//    }
////}
//#include <stdio.h>
//int main()
//{
//    int a,i,j;
//    scanf("%d", &a);
//    for(i=1;i<=a;i++){ //세로반복
//        for(j=1;j<=i;j++){ //가로반복
//            printf("*");
//        }
//        printf("\n"); // 줄바꾸기
//    }
//}
//1351
//#include <stdio.h>
//int main()
//{
//    int a,b,i,j;
//    scanf("%d %d",&a,&b);
//    for(i=a;i<=b;i++){
//        for(j=1;j<=9;j++){
//            printf("%d*%d=%d\n",i,j,i*j);
//        }
//    }
//}
//1403
//#include <stdio.h>
//int main()
//{
//    int a, i;
//    scanf("%d",&a);
//    int arr[a];
//    for(i=0; i<a; i++){
//        scanf("%d",&arr[i]);
//    }
//    for(i=0; i<a; i++){
//        printf("%d\n",arr[i]);
//    }
//    for(i=0; i<a; i++){
//        printf("%d\n",arr[i]);
//    }
//
//
//}
//#include <stdio.h>
//int main()
//{
//    int a, i;
//    int *p;
//    scanf("%d",&a);
//    int arr[a];
//    p = arr; //&arr[0]
//    for(i=0; i<a; i++){
//        scanf("%d",p+i);
//    }
//    for(i=0; i<a; i++){
//        printf("%d\n",*(p+i));
//    }
//    for(i=0; i<a; i++){
//        printf("%d\n",*(p+i));
//    }
//}
//4561
#include <stdio.h>
int main()
{
    int arr[7];
    int a, i;
    int sum = 0;
    int min=100;
    int *p;

    for(i=0;i<7; i++){
        scanf("%d", &arr[i]);
    }
    p=arr;
    for(i=0;i<7;i++){
        if(*(p+i)%2==1){
            sum=sum+*(p+i);
            if(*(p+i)<min){
                min =*(p+i);
            }
        }
    }
    if(sum==0){
        printf("-1");
    }else{
        printf("%d\n",sum);
        printf("%d",min);
    }
}
