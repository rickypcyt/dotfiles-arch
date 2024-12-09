# ~/.config/hypr/restore_windows.sh
# Lee el archivo de aplicaciones guardadas y las ejecuta
if [ -f ~/.config/hypr/windows.txt ]; then
    while read -r app; do
        # Ejemplo: Ejecuta aplicaciones por su nombre (ajusta según tus necesidades)
        nohup $app &
    done < ~/.config/hypr/windows.txt
fi
