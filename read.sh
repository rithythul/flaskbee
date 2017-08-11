echo "what is the project?"

read project

mkdir $project

cd  $project

cat <<EOF | nano hello.txt 
    Hello I am a new file. 
EOF

