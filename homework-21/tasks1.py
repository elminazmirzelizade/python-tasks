#1. kart = “5382-1739-9201-9017” bank kartı məlumatını daşıyan variablein ilk 8 nömrəsini ulduzlanmış şəkildə print edin.
# kart = '5382-1739-9201-9017'
print(kart[-10:].rjust(18,'*'))
#2. 15 ədədinin 4-ə bölünməsindən çıxan qalığın kubunu tapın
print(divmod(15,4)[1]**3)
#3. 256.91872 ədədinin nöqtədən sonrakı və əvvəlki 2-ci ədədə qədər yuvarlaqlaşdırın. (2 fərqli cavab almalısınız)
# a=256.91872 
print(round(a,1))
print(round(a,-2))
#4. 34 ədədinin əvvəlinə string metodlarının köməyilə 3 sıfır əlavə edin
a=34
print(str(a).zfill(5))
#5. Girilən floatın tam hissəsinin neçə ədəddən ibarət olduğunu göstərən program hazırlayın. Bunun üçün input və print funksiyalarından istifadə edin.
eded=float(input('ededi daxil edin:'))
print(len(str(int(eded))))
#6. Girilən websaytın əvvəlindəki https:// və sonundakı .com hissələrini silən və istifadəçiyə göstərən program hazırlayın. (input və print ilə)
siteUrl = input('saytin url-ni daxil edin:')
removePrefix=siteUrl.removeprefix('https://')
print(removePrefix.removesuffix('.com'))
#7. İstifadəçi yazacağınız inputlar vasitəsilə dəyişmək istədiyi sözü, nəyə dəyişmək istədiyini və mətni daxil edəcək, qurduğunuz program isə mətndə həmin sözləri dəyişib istifadəçiyə print edəcək
sentence=input('metni daxil edin:')
word=input('deyismek istediyiniz sozu daxil edin:')
newWord=input('hansi soze deyimek istediyinizi qeyd edin:')
print(sentence.replace(word,newWord))
