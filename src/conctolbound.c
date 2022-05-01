#include <stdio.h>
#include "python3.6/Python.h"

void rendersigner(int A)
{
   // Begin_run++;
}

static PyObject * _rendersigner(PyObject *self, PyObject *args)
{
    int _a;
    int res;

    if (!PyArg_ParseTuple(args, "i", &_a))
        return NULL;
    res = rendersigner(_a);
    return PyLong_FromLong(res);
}

static PyMethodDef GreateModuleMethods[] = {
    {
        "rendersigner",
        _rendersigner,
        METH_VARARGS,
        ""
    },
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef sampleModule = {
PyModuleDef_HEAD_INIT,

"rendersigner", /* name of module */

"conctolbound.c", /* module documentation, may be NULL */

-1, /* size of per-interpreter state of the module,

or -1 if the module keeps state in global variables. */

GreateModuleMethods

};

// The initialization function must be named PyInit_name()

PyMODINIT_FUNC PyInit_sample(void)

{

return PyModule_Create(&sampleModule);

}
}
