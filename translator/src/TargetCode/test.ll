; ModuleID = "clong prog"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:o-i64:64-f80:128-n8:16:32:64-S128"

define i32 @"main"()
{
main.entry:
  %".2" = getelementptr inbounds [14 x i8], [14 x i8]* @".str0", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
}

declare i32 @"printf"(i8* %".1", ...)

@".str0" = constant [14 x i8] c"Hello World!\0a\00"