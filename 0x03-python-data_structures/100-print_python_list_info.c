#include <object.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;

	printf("[*] Size of Python List = %ld\n", Py_SIZE(list));
	printf("[*] Allocated = %ld\n", list->allocated);

	for (Py_ssize_t i = 0; i < Py_SIZE(list); ++i)
	{
		PyObject *item = PyList_GetItem(p, i);

		const char *item_type = item->ob_type->tp_name;

		printf("Element %ld: %s\n", i, item_type);
	}
}
