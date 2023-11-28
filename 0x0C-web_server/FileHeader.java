import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.FileVisitResult;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.HashSet;
import java.util.Set;

class FileHeader {
    public static void main(String[] arg) throws IOException {
        Files.walkFileTree(Path.of("."), new SimpleFileVisitor<Path>() {

            @Override
            public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
                var excludes = Set.of("./README.md", "./FileHeader.java", "./7-puppet_install_nginx_web_server.pp");
                if (excludes.contains(file.toString()))
                    return FileVisitResult.CONTINUE;
                
                File fil = file.toFile();
                if (fil.exists()) {
                    try (FileWriter fileWriter = new FileWriter(fil)) {
                        fileWriter.write("#!/usr/bin/env bash");
                    }
                }

                return FileVisitResult.CONTINUE;
            }
        });
    }
}
