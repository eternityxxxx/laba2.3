#pragma once

#ifdef MYDLL_EXPORTS
#define MYDLL_API __declspec(dllexport)
#else
#define MYDLL_API __declspec(dllimport)
#endif


extern "C" MYDLL_API char* FuncName();


extern "C" MYDLL_API double TheFunc(double x);

