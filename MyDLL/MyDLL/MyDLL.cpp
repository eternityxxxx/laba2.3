#include "pch.h"
#include <utility>
#include <limits.h>
#include "MyDLL.h"

char* FuncName() {
	char func[6] = { 'y', '=', 'x', '+', '2', 0};
	return func;
}

double TheFunc(double x) {
	return x + 2;
}