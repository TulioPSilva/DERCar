echo Criando diretorios...
echo ******************************

cd C:/
cd Action.NET
md ProjectsPython
cd ProjectsPython
md DERCar
cd DERCar

echo Criando ambiente virtual Python...
echo ******************************

python -m venv venv

cd venv
cd Scripts

echo Inclua os arquivos .py 
echo (getAnalises, getElementPowerflow, getLines, getPowerflow) em C:/Action.NET/ProjectsPython/DERCar
echo ******************************

PAUSE

echo Inclua os arquivo (requirements.txt) em C:/Action.NET/ProjectsPython/DERCar/venv/Scripts
echo ******************************

PAUSE

echo Ativando ambiente virtual Python...
echo ******************************

call activate.bat

echo Finalizando processo...
echo ******************************

pip install -r requirements.txt

echo FIM
PAUSE

