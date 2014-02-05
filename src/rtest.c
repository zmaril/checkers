#include <Python.h>

/* rtest


 Moves the red checkers. This calculates one turn for the "game"
 routine below.

 input:
       x1, y1 - Coordinates of the ascending black checker
       x2, y2 - Coordinates of the descending black checker
       R - List of red checker positions
       n - Dimension of the board

	output:
       R - Updated list of red checker positions
       sp - "1" if a split occured, "0" otherwise
*/

static PyObject* rtest(PyObject* self, PyObject* args)
{
	int x1, y1, x2, y2, n;
	int i, length;
	PyObject* R;

	if (!PyArg_ParseTuple(args,"iiiiOi", &x1, &y1, &x2, &y2, &R, &n))
		return NULL;
	length = PyList_Size(R);
	long r[length+n];

	for (i=0; i<length;i++){
		r[i] = PyInt_AsLong(PyList_GetItem(R,i));
 	}

	int greek = 2, roman=2, sp = 0;
	int cr=-1, cd=-1;
	int col;
	for (col = n-1; col > x2-1; col--){
		if (r[col] == y2){
			cr = col;
			if (col == x2)
				greek = 0;
			else
				greek = 1;
		}
	}

	for (col = x2-1; col > -1; col--){
		if (x2-col+r[col] == n){
			cd = col;
			if (y1 == r[col] && x1 == col){
				roman = 0;
			}
			else{
				roman = 1;
			}
		}
	}

	if (roman == 0){
		r[x1]=r[x1]-1;
		if (greek == 0){
			r[x2] += 1;
		}
		if(greek == 1){
			r[cr] += 1;
		}
	}

	if (roman == 1){
		if (greek == 0){
			r[cr] = r[cd];
			r[cd] = 99;
			r[x1]= y2;
		}
		if(greek == 1){
			int block = 0;
			for (i = cr-1; i > cd; i--){
				if (r[cr] < r[i] && r[i] < r[cd]){
						block = 1;
					}
			}
			if (block != 1){
				sp = 1;
			}
		}
	}
	if (roman == 2 && greek == 0){
		r[x1]=r[cr];
		r[cr]=99;
	}
	PyObject* answer = PyList_New(length);
	for (i = 0; i < length; i++){
		PyList_SetItem(answer,i, Py_BuildValue("i",r[i]));
	}
	if (sp == 1){
		for (i = 0; i < n; i++){
			PyList_Append(answer,Py_BuildValue("i",r[i]));
		}
    PyList_SetItem(answer,length+cr,Py_BuildValue("i",r[cd]));
    PyList_SetItem(answer,length+cd,Py_BuildValue("i",(long) 99));
    PyList_SetItem(answer,length+x1,Py_BuildValue("i",(long) y2));
	}
	return Py_BuildValue("Oi",answer,sp);
}

static PyMethodDef RTestMethods[] =
	{
		{"rtest",rtest,METH_VARARGS, "Greet somebody."},
		{NULL,NULL,0,NULL}
	};

PyMODINIT_FUNC

initrtest(void)
{
	(void) Py_InitModule("rtest",RTestMethods);
}
