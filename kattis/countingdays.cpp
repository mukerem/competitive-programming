// https://open.kattis.com/problems/countingdays
// Time: 2022-09-16 16:15:18
// title: Counting Days
// language: C++


#include "countingdays.h"
int h=0, m=0, d=1;
void lookAtClock(int hours, int minutes) {
    if(h*60+m >= hours*60 + minutes){
        d++;
    }
    h = hours;
    m = minutes;
}

int getDay() {
    return d;
}