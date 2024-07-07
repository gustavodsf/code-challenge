package com.codility;

import java.util.*;
import java.util.stream.*;

class VisitCounter {

    Map<Long, Long> count(Map<String, UserStats>... visits) {
        if (visits == null){
            return new HashMap<>();
        }

        return Arrays.stream(visits)
                    .filter(Objects::nonNull)
                    .flatMap(visitMap -> visitMap.entrySet().stream())
                    .filter(entry -> isValidEntry(entry))
                    .collect(Collectors.toMap(
                        entry -> Long.parseLong(entry.getKey()),
                        entry -> entry.getValue().getVisitCount().get(),
                        Long::sum
                    ));
    }

    private boolean isValidEntry(Map.Entry<String, UserStats> entry) {
        if( entry.getValue() == null){
            return false;
        }
        if( !entry.getValue().getVisitCount().isPresent()){
            return false;
        }
        try{
            Long.parseLong(entry.getKey());
        }catch( NumberFormatException e){
            return false;
        }
        return true;
    }
}
