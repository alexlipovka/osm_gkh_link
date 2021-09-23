trim(
	replace(
	replace(
	replace(
	replace(
	replace(
	replace(
	replace(
	replace(
	replace(
	replace(
	replace(
	replace(if("addr:street" = '', if( "addr:suburb" = 'Академгородок',  "addr:suburb", ''),  "addr:street" )
	, 'улица', '')
	, 'проспект', '') 
	, 'проезд',  '')
	, '.', '')
	, 'ё', 'е')
	, 'набережная', '')
	, 'переулок', '')
	, 'имени ', '')
	, 'им ', '')
	, '60 лет Образования', '60 лет образования')
	, 'Солнечный бульвар',  'Солнечный Бульвар')
	, 'Льва Толстого',  'Толстого')
	)
	
+ ' ' + upper(
	replace("addr:housenumber"
		, '/', ' к')
	)