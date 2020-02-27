for file in *.zip;do
	path='/home/ch/pybites'
	dirname=${file/pybites_bite};
	dirname=${dirname%.zip};
	archive="$path/archive"
	if [ ! -d "$path/$dirname" ];then
	      unzip -d "$path/$dirname" $file;
	fi

done

