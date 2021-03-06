from textwrap import TextWrapper as TxtWrpr 

str_Dflt_CmpyNm = 'BRG'
str_Dflt_ProdNm = 'CompasGH'
str_Dflt_TitPfx = str_Dflt_ProdNm 

def GenerateStringRepresentation(CGHObj, dct_AddtlInfo = None, str_TitPfx = str_Dflt_TitPfx):
	def _DisplayAttribute (nm, val):
		_nSpc_1 = 2
		_nSpc_2 = 40
		_str_AttrDisp 		= ' '*_nSpc_1 #len(str(nm))
		if isinstance(_val, float):
			_str_AttrDisp 	+= '{_nm} : {_val:.3f}'.format(_nm=_nm, _val=_val) #rounding
		elif isinstance (_val, int):
			_str_AttrDisp 	+= '{_nm} : {_val:d}'.format(_nm=_nm, _val=_val)
		elif isinstance (_val, str):
			_str_AttrDisp 	+= '{_nm} : {_val}'.format(_nm=_nm, _val=_val) 
		return _str_AttrDisp;

	if hasattr(CGHObj, 'ToStringClassNameOverride'):
		_str_ClsNm 			= CGHObj.ToStringClassNameOverride()
	else:
		_str_ClsNm 			= CGHObj.__class__.__name__

	_str_Tit 		= '[[ ' + str_TitPfx + " :: " + _str_ClsNm + ' ]]'

	_str_AttrsDisp	= ''
	if dct_AddtlInfo is not None:
		for _nm, _val in dct_AddtlInfo.items():
			_str_AttrsDisp += '\n'
			_str_AttrsDisp += _DisplayAttribute(_nm, _val)
	
	_str_Otp		= _str_Tit + _str_AttrsDisp
	return _str_Otp;

def FormatFloatsList (dtaL, n_Decml=3):
	str_FmtdL = 	'['
	for _v in dtaL:
		str_FmtdL += ' {_v:.{_n_Decml}f} ,'.format(_v=_v, _n_Decml=n_Decml)
	str_FmtdL = 	str_FmtdL[0:-1]
	str_FmtdL += 	']'
	return str_FmtdL

def ConcatenateValuesList(dtaL, str_Pfx='(', str_Sfx=')'):
	_str 	= str_Pfx
	_n_dta 	= len(dtaL) 
	for _i, _dta in enumerate(dtaL):
		_str += str(_dta)
		if _i < _n_dta - 1:
			_str += str(',')
	_str 	+= str_Sfx
	return _str

if __name__ == "__main__":
	# dtaL = [1.293551,2.596839,3.5938434]
	# strL = FormatFloatsList(dtaL)
	# print (strL)

	print (ConcatenateValuesList([1,2,3]))
	# class testDataStructureWithLongFancyName ():
	# 	def __init__(self):
	# 		pass

	# testObj = testDataStructureWithLongFancyName()
	# testAttrs = {'a': int(123), 'b':'hello'}

	# print (GenerateStringRepresentation(testObj, testAttrs))

