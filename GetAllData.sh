IFS=$'\r\n' GLOBIGNORE='*' command eval  'XYZ=($(cat data/listOfCodes.txt))'
years=("2002" "2012")
for year in "${years[@]}"
do
for i in "${XYZ[@]}"
do
echo ${i}
curl "http://api.census.gov/data/"${year}"/ewks?get=PAYANN,ESTAB,EMP&for=county:*&in=state:*&NAICS"${year}"=$i&OPTAX=A&key=3d4047590356727bf89cab9124ab1340c179068c" > data/${year}/${i}.txt
done
done