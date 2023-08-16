#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: python object.
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size_p, allocated, i = 0;
	PyObject *element;

	size_p = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size_p);
	printf("[*] Allocated = %ld\n", allocated);
	while (i < size_p)
	{
		element = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, element->ob_type->tp_name);
		i++;
	}
}
