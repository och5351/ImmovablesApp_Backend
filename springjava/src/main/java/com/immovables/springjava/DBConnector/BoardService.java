package com.immovables.springjava.DBConnector;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;

@Service
public class BoardService {

    @Autowired
    private BoardRepository boardRepository;

    public BoardEntity getBoard(Long boardId) {
        return boardRepository.findById(boardId)
                .orElseThrow(() -> new RestException(HttpStatus.NOT_FOUND, "Not found board"));
    }

}
