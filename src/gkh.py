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
replace(
replace(
replace(
replace(
replace(
replace(
	"formalname_street"
	, 'им ', '')
	, 'Героя Советского Союза ', '')
	, 'А.Д.Кравченко', 'Кравченко')
	, 'Корнетова Дружинника', 'Корнетова')
	, '52 Квартал', '52-й квартал')
	, 'Краснофлотская 2-я', '2-я Краснофлотская')
	, 'Огородная 2-я', '2-я Огородная')
	, 'Курчатова', 'Академика Курчатова')
	, 'Хабаровская 1-я', '1-я Хабаровская')
	, 'Хабаровская 2-я', '2-я Хабаровская')
	, 'П.И.Словцова', 'Петра Словцова')
	, 'Е.Д.Стасовой', 'Елены Стасовой')
	, 'В.В.Вильского', 'Вильского')
	, 'М.А.Юшкова', 'Юшкова')
	, 'Н.Я.Тотмина', 'Тотмина')
	, 'Д.М.Карбышева', 'Карбышева')
	, 'Ивана Забобонова', 'Забобонова')
	, 'П.М.Петрушина', 'Петрушина')
	, 'Б.А.Микуцкого', 'Микуцкого')
	, 'И.А.Борисевича', 'Борисевича')
	, 'Космонавта Быковского', 'Быковского')
	, 'Космонавта Терешковой', 'Терешковой')
	, 'Писателя Н.Устиновича', 'Устиновича')
	, 'В.М.Комарова', 'Комарова')
	, 'Космонавта Николаева', 'Николаева')
	, 'Краснофлотская 2-я', '2-я Краснофлотская')
	, 'Н.Н.Урванцева', 'Урванцева')
	, 'Б.З.Шумяцкого', 'Шумяцкого')
	
 + ' ' +  
 upper(
	replace(
	
	replace(
	replace(
	replace(
	replace("house_number"
		, 'дом ', '')
		, 'д.', '')
		, ' ', '')
		, '/', ' к')
		
	+  
	
	if("building" is not null,
	replace(
	replace(
	replace("building"
		, 'общ', '')
		, 'нет', '')
		, 'исправный', '')
	, '')
	
	+ 
	
	if("block" is not null,
		if(	length(regexp_substr("block", '(\\d+)')) > 0, ' к' + "block",
		replace(
		replace("block"
			, 'общ', '')
			, 'нет', '')
			)		
	, '')
	
	+  "letter"
	, '-', '')
	)