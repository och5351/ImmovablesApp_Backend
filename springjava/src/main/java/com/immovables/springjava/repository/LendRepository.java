package com.immovables.springjava.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;
import com.immovables.springjava.model.entity.Book;
import com.immovables.springjava.model.entity.Lend;
import com.immovables.springjava.model.entity.LendStatus;

public interface LendRepository extends JpaRepository<Lend, Long> {
    Optional<Lend> findByBookAndStatus(Book book, LendStatus status);
}