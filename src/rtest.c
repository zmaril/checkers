#include <Python.h>

static PyObject* rtest(PyObject* self, PyObject* args)
{
	int x1, y1, x2, y2, n;
	int i;
	PyObject* R; 
 
	if (!PyArg_ParseTuple(args,"iiiiOi", &x1, &y1, &x2, &y2, &R, &n))
		return NULL;

	/* printf("c  %d %d %d %d [",x1,y1,x2,y2); */
	/* for (i = 0; i < PyList_Size(R)-1; i++){ */
	/* 	printf("%d, ",PyInt_AsLong(PyList_GetItem(R,i))); */
	/* } */
	/* printf("%d] %d\n",PyInt_AsLong(PyList_GetItem(R,i)),n); */

	int greek = 2, roman=2, sp = 0;
	int cr=-1, cd=-1;
	int col;
	for (col = n-1; col > x2-1; col--){
		/* printf("c  col %d n %d x2-1 %d\n",col,n,x2-1); */
		/* printf("c  cr %d greek %d roman %d\n",cr, greek,roman); */
		if (PyInt_AsLong(PyList_GetItem(R,col)) == y2){
			cr = col;
			if (col == x2)
				greek = 0;
			else
				greek = 1;
		}		
	}
	
	for (col = x2-1; col > -1; col--){
		/* printf("c  col %d n %d x2-1 %d\n",col,n,x2-1); */
		/* printf("c  cr %d greek %d roman %d\n",cr, greek,roman); */
		if (x2-col+PyInt_AsLong(PyList_GetItem(R,col)) == n){
			cd = col;
			if (y1 == PyInt_AsLong(PyList_GetItem(R,col)) && x1 == col){
				roman = 0;
			}
			else{
				roman = 1;
			}
		}
	}		
	
	/* printf("c  cd %d cr %d greek %d roman %d\n",cd,cr, greek,roman); */
	PyObject* t;
	if (roman == 0){
		t = Py_BuildValue("i",PyInt_AsLong(PyList_GetItem(R,x1))-1);
		PyList_SetItem(R,x1,t);

		if (greek == 0){
			t = Py_BuildValue("i",PyInt_AsLong(PyList_GetItem(R,x2))+1);
			PyList_SetItem(R,x2,t);
		}
		if(greek == 1){
			t = Py_BuildValue("i",PyInt_AsLong(PyList_GetItem(R,cr))+1);
			PyList_SetItem(R,cr,t);
		}
	}

	if (roman == 1){
		if (greek == 0){
			/* printf("c  %d %d %d %d [",x1,y1,x2,y2); */
			/* for (i = 0; i < PyList_Size(R)-1; i++){ */
			/* 	printf("%d, ",PyInt_AsLong(PyList_GetItem(R,i))); */
			/* } */
			/* printf("%d] %d\n",PyInt_AsLong(PyList_GetItem(R,i)),n); */

			PyList_SetItem(R,cr,PyList_GetItem(R,cd));
			PyList_SetItem(R,cd,Py_BuildValue("i",(long) 99));
			PyList_SetItem(R,x1,Py_BuildValue("i",(long) y2));
		}
		if(greek == 1){
			int block = 0;
			//			printf("c  cd %d cr %d\n",cd,cr);
			for (i = cr-1; i > cd; i--){
				//				printf("c  %d");
				long t = PyInt_AsLong(PyList_GetItem(R,i));
				if(PyInt_AsLong(PyList_GetItem(R,cr)) < t &&
					 t < PyInt_AsLong(PyList_GetItem(R,cd))){
					block = 1;
				}
			}
			if (block != 1){
				int len = PyList_Size(R);
				for (i = 0; i < n; i++){
					PyList_Append(R,PyList_GetItem(R,i));
				}
				PyList_SetItem(R,len+cr,PyList_GetItem(R,cd));
				PyList_SetItem(R,len+cd,Py_BuildValue("i",(long) 99));
				PyList_SetItem(R,len+x1,Py_BuildValue("i",(long) y2));
				sp = 1;
			}
		}
	}
	if (roman == 2 && greek == 0){
		PyList_SetItem(R,x1,PyList_GetItem(R,cr));
		PyList_SetItem(R,cr,Py_BuildValue("i",(long) 99));
	}
	/* printf("c  sp %d [",sp); */
	/* for (i = 0; i < PyList_Size(R)-1; i++){ */
	/* 	printf("%d, ",PyInt_AsLong(PyList_GetItem(R,i))); */
	/* } */
	/* printf("%d] \n",PyInt_AsLong(PyList_GetItem(R,i))); */
	return Py_BuildValue("Oi",R,sp);
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
