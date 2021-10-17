package com.immovables.springjava.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;
import com.immovables.springjava.model.entity.Book;

public interface BookRepository extends JpaRepository<Book, Long> {
    Optional<Book> findByIsbn(String isbn);
}