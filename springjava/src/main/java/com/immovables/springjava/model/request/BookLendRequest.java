package com.immovables.springjava.model.request;

import java.util.List;

import lombok.Data;

@Data
public class BookLendRequest {
    private Long bookIds;
    private Long memberId;
}