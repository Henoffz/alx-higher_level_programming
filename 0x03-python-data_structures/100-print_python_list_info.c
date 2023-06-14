#include "Python.h"
#include <stdio.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: python object.
 */
void print_python_list_info(PyObject *p)
{
	ssize_t size;
	ssize_t allocated;
	ssize_t i;
	const char *type_name = NULL;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);
	
	for (i = 0; i < size; i+)
	{
		PyObject *element = PyList_GetItem(p, i);
		type_name = Py_TYPE(element)->tp_name;
		
		printf("Element %zd: %s\n", i, type_name);
	}
}

