# Share-price-forecasing
Прогнозирование роста/падения котировок по новостному контенту

## Постановка задачи
Определить, какую тенденцию (рост или падение) будут иметь котировки акции  
российской компании в течение периода *T* после публикации о ней новостной статьи.  

*X* - текстовое содержание новостной публикации;  
*Y* - класс 0/1 (тенденция роста/падения).  

Класс *Y* определяется следующим образом:
```
Y = 0, если a > 0;
Y = 1, если a < 0;
```
*a* - коэффициент линейной регрессии котировок акции на временной интервал *(1, T)*.  
Знак при коэффициенте - индикатор восходящего или нисходящего тренда.

## Источники данных
Новостные статьи получены с портала [Investing.com](https://ru.investing.com/)  
Котировки акций - взяты с сайта [Yahoo.com](https://finance.yahoo.com/)

Каждая новостная статья сопровождается датой публикации и названием компании.  
Эти атибуты необходимы для расчета коэффициента линейной регрессии *a*.  

Всего собрано 70 660 новостных статей о 32-х российских компаниях, входящих в РТС.
