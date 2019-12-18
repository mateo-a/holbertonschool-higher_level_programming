#include "lists.h"
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: Python object
 */

void print_python_list_info(PyObject *p)
{
	int i;
	PyObject *item;

	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < Py_SIZE(p); i++)
		{
			item = PyList_GetItem(p, i);
			printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
}
