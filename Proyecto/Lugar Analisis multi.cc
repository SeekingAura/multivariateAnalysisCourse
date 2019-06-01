=SI(O(
		Y('defuncion risaralda 2017'!C2=1;'defuncion risaralda 2017'!B2=1);
		Y('defuncion risaralda 2017'!C2=1;'defuncion risaralda 2017'!B2=3);
		Y('defuncion risaralda 2017'!C2=2;'defuncion risaralda 2017'!B2=1)
	);
	'defuncion risaralda 2017'!F2&"/"&'defuncion risaralda 2017'!A2;
	
		SI(Y('defuncion risaralda 2017'!C2=3;'defuncion risaralda 2017'!B2=1);
		"Casa Cabecera Municipal"&"/"&'defuncion risaralda 2017'!A2;
			
			SI(Y('defuncion risaralda 2017'!C2=3;'defuncion risaralda 2017'!B2=2);
			"Casa Centro Poblado"&"/"&'defuncion risaralda 2017'!A2;
				
				SI(Y('defuncion risaralda 2017'!C2=3;'defuncion risaralda 2017'!B2=3);
				"Casa Rural"&"/"&'defuncion risaralda 2017'!A2;
					
					SI('defuncion risaralda 2017'!C2=6;
					'defuncion risaralda 2017'!D2&"/"&'defuncion risaralda 2017'!A2;

						SI('defuncion risaralda 2017'!C2=5;
						"Ambulancia"&"/"&'defuncion risaralda 2017'!A2;
							"otro"
						)	
					)
				)	
			)	
		)
)